# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2050?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2050
- Title: ASSIST Act
- Congress: 119
- Bill type: S
- Bill number: 2050
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-07-25T16:16:08Z
- Update date including text: 2025-07-25T16:16:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2050",
    "number": "2050",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "ASSIST Act",
    "type": "S",
    "updateDate": "2025-07-25T16:16:08Z",
    "updateDateIncludingText": "2025-07-25T16:16:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T15:46:15Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NM"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MN"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2050is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2050\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Warnock (for himself, Mr. Padilla , Mr. Luj\u00e1n , Ms. Smith , Ms. Alsobrooks , Mr. Welch , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Social Security Act to provide for an increased Federal medical assistance percentage for State expenditures on certain behavioral health services furnished under the Medicaid program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Student Services In Schools Today Act or the ASSIST Act .\n#### 2. Increasing the applicable FMAP for State expenditures attributable to certain behavioral health services\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended\u2014\n**(1)**\nin subsection (b), by striking and (ii) and inserting (ii), and (kk) ; and\n**(2)**\nby adding at the end the following new subsection:\n(kk) Increased FMAP for medical assistance for services furnished by mental health and substance use disorder care providers in certain school-Based settings (1) In general Notwithstanding any preceding provision of this section, with respect to State expenditures for medical assistance consisting of services provided by a mental health and substance use disorder care provider (as defined in section 3 of the Advancing Student Services In Schools Today Act ) and furnished at a school or at a school-based health center (as defined in section 399Z\u20131(a)(3) of the Public Health Service Act) on or after the first day of the first calendar quarter beginning on or after the date that is 12 months after the date of the enactment of this subsection, the Federal medical assistance percentage otherwise determined under subsection (b) shall, subject to paragraph (2), be equal to 90 percent. (2) Application of higher match Paragraph (1) shall not apply in the case of State expenditures described in such paragraph if application of such paragraph would result in a lower Federal medical assistance percentage for such expenditures than would otherwise apply without application of such paragraph. (3) Exclusion of expenditures from territorial cap Any payment made to a territory for expenditures for medical assistance described in paragraph (1) that are subject to the Federal medical assistance percentage specified under such paragraph shall not be taken into account for purposes of applying payment limits under subsections (f) and (g) of section 1108 to the extent that such payment exceeds the amount of the payment that would have been made to the territory for such expenditures without regard to this subsection. .\n#### 3. Program to increase mental health and substance use disorder care providers in schools and school-based health centers\n##### (a) Findings\nCongress finds that the lack of access to mental health and substance use disorder care in schools and school-based health centers has a negative impact on the health of children in the United States, including children who are eligible for coverage under the Medicaid and Children's Health Insurance Program.\n##### (b) Grant authority\nNot later than 12 months after the date of enactment of this Act, the Secretary of Health and Human Services (referred to in this section as the Secretary ), in consultation with the Administrator of the Centers for Medicare & Medicaid Services and the Secretary of Education, shall award grants, contracts, or cooperative agreements to eligible entities to increase the number of mental health and substance use disorder care providers in schools and school-based health centers served by such entities.\n##### (c) Application\nAn eligible entity seeking an award under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including a description of\u2014\n**(1)**\nthe mental health and substance use disorder needs of the student population served by the eligible entity; and\n**(2)**\nwith respect to the student population served by the eligible entity, how the eligible entity will ensure that the mental health and substance use disorder care providers supported by the eligible entity, and the services administered by such providers, are culturally competent and linguistically appropriate.\n##### (d) Restriction\nNo funds made available through an award under this section may be used for a threat assessment team.\n##### (e) Reporting\n**(1) Eligible entity reporting**\nEligible entities receiving an award under this section shall submit an annual report to the Secretary accompanied by such information as the Secretary may require, including\u2014\n**(A)**\nthe number of mental health and substance use disorder care providers working at the schools or school-based health centers served by the eligible entity, and the number of such providers supported through the award;\n**(B)**\nthe types of services provided by the mental health and substance use disorder care providers and the efficacy of such services;\n**(C)**\nthe practices used by the schools or school-based health centers served by the eligible entity to recruit and retain mental health and substance use disorder care providers; and\n**(D)**\nthe rates of retention of mental health and substance use disorder care providers at the school or school-based health center.\n**(2) Secretary**\nNot later than 18 months after the date of enactment of this section, and every 5 years thereafter, the Secretary shall submit to Congress a report on the effectiveness of the awards under this section.\n##### (f) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na local educational agency, as defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 );\n**(B)**\nan institution of higher education, as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 );\n**(C)**\na school operated by the Bureau of Indian Affairs; or\n**(D)**\na school-based health center, as defined in section 399Z\u20131(a)(3) of the Public Health Service Act ( 42 U.S.C. 280h\u20135(a)(3) ).\n**(2) Mental health and substance use disorder care provider**\nThe term mental health and substance use disorder care provider means an individual who is licensed or credentialed to provide mental health and substance use disorder services, including\u2014\n**(A)**\na school counselor;\n**(B)**\na school psychologist or any other psychologist;\n**(C)**\na psychiatrist who specializes in child or adolescent psychiatry;\n**(D)**\na school social worker;\n**(E)**\na peer support specialist or peer recovery coach;\n**(F)**\na licensed clinical social worker;\n**(G)**\nan addiction medicine specialist; and\n**(H)**\nother providers, as the Secretary determines appropriate.",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-07-08T13:13:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s2050",
          "measure-number": "2050",
          "measure-type": "s",
          "orig-publish-date": "2025-06-12",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2050v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Advancing Student Services In Schools Today Act or the ASSIST Act</strong></p><p>This bill establishes programs and requirements to support the provision of mental health and substance use disorder services at schools.</p><p>Specifically, the bill provides for a 90% Federal Medical Assistance Percentage (i.e., federal matching rate) under Medicaid for services that are furnished by mental health and substance use disorder providers at schools or school-based health centers. Qualifying services include those provided by school counselors, social workers, and psychologists.\u00a0</p><p>The bill also establishes a grant program to increase the number of mental health and substance use disorder providers at schools, colleges, and other educational institutions.</p>"
        },
        "title": "ASSIST Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2050.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Advancing Student Services In Schools Today Act or the ASSIST Act</strong></p><p>This bill establishes programs and requirements to support the provision of mental health and substance use disorder services at schools.</p><p>Specifically, the bill provides for a 90% Federal Medical Assistance Percentage (i.e., federal matching rate) under Medicaid for services that are furnished by mental health and substance use disorder providers at schools or school-based health centers. Qualifying services include those provided by school counselors, social workers, and psychologists.\u00a0</p><p>The bill also establishes a grant program to increase the number of mental health and substance use disorder providers at schools, colleges, and other educational institutions.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s2050"
    },
    "title": "ASSIST Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Advancing Student Services In Schools Today Act or the ASSIST Act</strong></p><p>This bill establishes programs and requirements to support the provision of mental health and substance use disorder services at schools.</p><p>Specifically, the bill provides for a 90% Federal Medical Assistance Percentage (i.e., federal matching rate) under Medicaid for services that are furnished by mental health and substance use disorder providers at schools or school-based health centers. Qualifying services include those provided by school counselors, social workers, and psychologists.\u00a0</p><p>The bill also establishes a grant program to increase the number of mental health and substance use disorder providers at schools, colleges, and other educational institutions.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s2050"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2050is.xml"
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
      "title": "ASSIST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T06:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ASSIST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T06:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advancing Student Services In Schools Today Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T06:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Social Security Act to provide for an increased Federal medical assistance percentage for State expenditures on certain behavioral health services furnished under the Medicaid program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:24Z"
    }
  ]
}
```
