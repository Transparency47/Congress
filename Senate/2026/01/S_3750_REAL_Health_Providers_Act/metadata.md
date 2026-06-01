# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3750?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3750
- Title: REAL Health Providers Act
- Congress: 119
- Bill type: S
- Bill number: 3750
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-26T18:26:37Z
- Update date including text: 2026-02-26T18:26:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3750",
    "number": "3750",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "REAL Health Providers Act",
    "type": "S",
    "updateDate": "2026-02-26T18:26:37Z",
    "updateDateIncludingText": "2026-02-26T18:26:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-01-30T01:19:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "OR"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3750is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3750\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Bennet (for himself, Mr. Tillis , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to establish provider directory requirements, and to provide accountability for provider directory accuracy, under Medicare Advantage.\n#### 1. Short title\nThis Act may be cited as the Requiring Enhanced and Accurate Lists of Health Providers Act or the REAL Health Providers Act .\n#### 2. Provider directory requirements under Medicare Advantage\n##### (a) In general\nSection 1852(c) of the Social Security Act ( 42 U.S.C. 1395w\u201322(c) ) is amended\u2014\n**(1)**\nin paragraph (1)(C)\u2014\n**(A)**\nby striking plan, and any and inserting plan, any ; and\n**(B)**\nby inserting the following before the period: , and, in the case of a specified MA plan (as defined in paragraph (3)(C)), for plan year 2028 and subsequent plan years, the information described in paragraph (3)(B) ; and\n**(2)**\nby adding at the end the following new paragraph:\n(3) Provider directory accuracy (A) In general For plan year 2028 and subsequent plan years, each MA organization offering a specified MA plan (as defined in subparagraph (C)) shall, for each such plan offered by the organization\u2014 (i) maintain, on a publicly available internet website, an accurate provider directory that includes the information described in subparagraph (B); (ii) not less frequently than once every 90 days (or, in the case of a hospital or any other facility determined appropriate by the Secretary, at a lesser frequency specified by the Secretary but in no case less frequently than once every 12 months), verify the provider directory information of each provider listed in such directory and, if applicable, update such information; (iii) if the organization is unable to verify such information with respect to a provider, include in such directory an indication that the information of such provider may not be up to date; and (iv) remove a provider from such directory within 5 business days if the organization determines that the provider is no longer a provider participating in the network of such plan. (B) Provider directory information The information described in this subparagraph is information enrollees may need to access covered benefits from a provider with which such organization offering such plan has an agreement for furnishing items and services covered under such plan, such as name, specialty, contact information, primary office or facility addresses where items or services are furnished, whether the provider is accepting new patients, accommodations for people with disabilities, cultural and linguistic capabilities, and telehealth capabilities. (C) Specified MA plan In this paragraph, the term specified MA plan means\u2014 (i) a network-based plan (as defined in subsection (d)(5)(C)); or (ii) a Medicare Advantage private fee-for-service plan (as defined in section 1859(b)(2)) that meets the access standards under subsection (d)(4), in whole or in part, through entering into contracts or agreements as provided for under subparagraph (B) of such subsection. .\n##### (b) Accountability for provider directory accuracy\n**(1) Cost Sharing for Services Furnished Based on Reliance on Incorrect Provider directory Information**\nSection 1852(d) of the Social Security Act ( 42 U.S.C. 1395w\u201322(d) ) is amended\u2014\n**(A)**\nin paragraph (1)(C)\u2014\n**(i)**\nin clause (ii), by striking or at the end;\n**(ii)**\nin clause (iii), by striking the semicolon at the end and inserting , or ; and\n**(iii)**\nby adding at the end the following new clause:\n(iv) for plan year 2028 and subsequent plan years, in the case of a specified MA plan (as defined in subsection (c)(3)(C)), the services were furnished by a provider that was not participating in the network of such plan but was listed in the provider directory of such plan on the date on which the appointment was made, as described in paragraph (7)(A); ; and\n**(B)**\nby adding at the end the following new paragraph:\n(7) Cost sharing for services furnished based on reliance on incorrect provider directory information (A) In general For plan year 2028 and subsequent plan years, if an enrollee in a specified MA plan (as defined in subsection (c)(3)(C)) is furnished an item or service by a provider that is not participating in the network of such plan but is listed in the provider directory of such plan (as required to be provided to an enrollee pursuant to subsection (c)(1)(C)) on the date on which the appointment is made, and if such item or service would otherwise be covered under such plan if furnished by a provider that is participating in the network of such plan, the MA organization offering such plan shall ensure that the enrollee is only responsible for the lesser of\u2014 (i) the amount of cost sharing that would apply if such provider had been participating in the network of such plan; or (ii) the amount of cost sharing that would otherwise apply (without regard to this subparagraph). (B) Notification requirement For plan year 2028 and subsequent plan years, each MA organization that offers a specified MA plan shall\u2014 (i) notify enrollees of their cost-sharing protections under this paragraph and make such notifications, to the extent practicable, by not later than the first day of an annual, coordinated election period under section 1851(e)(3) with respect to a year; (ii) include information regarding such cost-sharing protections in the provider directory of each specified MA plan offered by the MA organization; and (iii) notify enrollees of their cost-sharing protections under this paragraph in the first explanation of benefits issued in a plan year. .\n**(2) Required provider directory accuracy analysis and reports**\n**(A) In general**\nSection 1857(e) of the Social Security Act ( 42 U.S.C. 1395w\u201327(e) ) is amended by adding at the end the following new paragraph:\n(6) Provider directory accuracy analysis and reports (A) In general Beginning with plan years beginning on or after January 1, 2028, subject to subparagraph (C), a contract under this section with an MA organization shall require the organization, for each specified MA plan (as defined in section 1852(c)(3)(C)) offered by the organization, to annually do the following: (i) Conduct an analysis estimating the accuracy of the provider directory information of such plan using a random sample of providers included in such provider directory as follows: (I) Such a random sample shall include a random sample of each specialty of providers with a high inaccuracy rate of provider directory information relative to other specialties of providers, as determined by the Secretary. (II) For purposes of subclause (I), one type of specialty may be providers specializing in mental health or substance use disorder treatment. (ii) Submit to the Secretary a report containing the results of the analysis conducted under clause (i), including an accuracy score for such provider directory information (as determined using a plan verification method specified by the Secretary under subparagraph (B)(i)). (B) Determination of accuracy score (i) In general The Secretary shall specify plan verification methods, such as using telephonic verification or other approaches using data sources maintained by an MA organization or using publicly available data sets, that MA organizations may use for estimating accuracy scores of the provider directory information of specified MA plans offered by such organizations. (ii) Accuracy score methodology With respect to each such method specified by the Secretary as described in clause (i), the Secretary shall specify a methodology for MA organizations to use in estimating such accuracy scores. Each such methodology shall take into account the administrative burden on plans and providers and the relative importance of certain provider directory information on enrollee ability to access care. (C) Exception The Secretary may waive the requirements of this paragraph in the case of a specified MA plan with low enrollment (as defined by the Secretary). (D) Transparency Beginning with plan years beginning on or after January 1, 2029, the Secretary shall post accuracy scores (as reported under subparagraph (A)(ii)), in a machine readable file, on an internet website maintained by the Centers for Medicare & Medicaid Services. .\n**(B) Provision of information to beneficiaries**\nSection 1851(d)(4) of the Social Security Act ( 42 U.S.C. 1395w\u201321(d)(4) ) is amended by adding at the end the following new subparagraph:\n(F) Provider Directory Beginning with plan years beginning on or after January 1, 2029, in the case of a specified MA plan (as defined in section 1852(c)(3)(C)), the accuracy score of the plan\u2019s provider directory (as reported under section 1857(e)(6)(A)(ii)) listed prominently on the plan\u2019s provider directory. .\n**(C) Funding**\nIn addition to amounts otherwise available, there is appropriated to the Centers for Medicare & Medicaid Services Program Management Account, out of any money in the Treasury not otherwise appropriated, $4,000,000 for fiscal year 2026, to remain available until expended, to carry out the amendments made by this paragraph.\n**(3) GAO study and report**\n**(A) Analysis**\nThe Comptroller General of the United States (in this paragraph referred to as the Comptroller General ) shall conduct a study of the implementation of the amendments made by paragraphs (1) and (2). To the extent data are available and reliable, such study shall include an analysis of\u2014\n**(i)**\nthe use of cost-sharing protections required under section 1852(d)(7)(A) of the Social Security Act, as added by paragraph (1);\n**(ii)**\nthe trends in provider directory information accuracy scores submitted to the Secretary of Health and Human Services under section 1857(e)(6)(A)(ii) of the Social Security Act (as added by paragraph (2)(A)), both overall and among providers specializing in mental health or substance use disorder treatment;\n**(iii)**\nprovider response rates by plan verification methods;\n**(iv)**\nadministrative costs to providers and Medicare Advantage organizations; and\n**(v)**\nother items determined appropriate by the Comptroller General.\n**(B) Report**\nNot later than January 15, 2033, the Comptroller General shall submit to Congress a report containing the results of the study conducted under subparagraph (A), together with recommendations for such legislation and administrative action as the Comptroller General determines appropriate.\n##### (c) Guidance on maintaining accurate provider directories\n**(1) Stakeholder meeting**\n**(A) In general**\nNot later than 6 months after the date of enactment of this Act, the Secretary of Health and Human Services (referred to in this subsection as the Secretary ) shall hold a public meeting to receive input on approaches for maintaining accurate provider directories for Medicare Advantage plans under part C of title XVIII of the Social Security Act ( 42 U.S.C. 1395w\u201321 et seq. ), including input on approaches for reducing administrative burden, such as data standardization, and best practices to maintain accurate provider directory information.\n**(B) Participants**\nParticipants of the meeting under subparagraph (A) shall include representatives from the Centers for Medicare & Medicaid Services and the Assistant Secretary for Technology Policy and Office of the National Coordinator for Health Information Technology. Such meeting shall be open to the public. To the extent practicable, the Secretary shall include health care providers, companies that specialize in relevant technologies, health insurers, and patient advocates.\n**(2) Guidance to Medicare Advantage organizations**\nNot later than 18 months after the date of enactment of this Act, the Secretary shall issue guidance to Medicare Advantage organizations offering Medicare Advantage plans under part C of title XVIII of the Social Security Act ( 42 U.S.C. 1395w\u201321 et seq. ) on maintaining accurate provider directories for such plans, taking into consideration input received during the stakeholder meeting under paragraph (1). Such guidance may include the following, as determined appropriate by the Secretary:\n**(A)**\nBest practices for Medicare Advantage organizations on how to work with providers to maintain the accuracy of provider directories and reduce provider and Medicare Advantage organization burden with respect to maintaining the accuracy of provider directories.\n**(B)**\nInformation on data sets and data sources with information that could be used by Medicare Advantage organizations to maintain accurate provider directories.\n**(C)**\nApproaches for utilizing data sources maintained by Medicare Advantage organizations and publicly available data sets to maintain accurate provider directories.\n**(D)**\nInformation that may be useful to include in provider directories for Medicare beneficiaries to use in assessing plan networks when selecting a plan and accessing providers participating in plan networks during the plan year.\n**(3) Guidance to part B providers**\nNot later than 12 months after the date of enactment of this Act, the Secretary shall issue guidance to providers of services and suppliers who furnish items or services for which benefits are available under part B of title XVIII of the Social Security Act ( 42 U.S.C. 1395j et seq. ) on when to update the National Plan and Provider Enumeration System (or a successor system) for information changes.",
      "versionDate": "2026-01-29",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-10",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5281",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "REAL Health Providers Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-02-26T18:26:37Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3750is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "REAL Health Providers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T11:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REAL Health Providers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Requiring Enhanced and Accurate Lists of Health Providers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to establish provider directory requirements, and to provide accountability for provider directory accuracy, under Medicare Advantage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:30Z"
    }
  ]
}
```
