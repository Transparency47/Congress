# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/502?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/502
- Title: Rural Hospital Closure Relief Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 502
- Origin chamber: Senate
- Introduced date: 2025-02-10
- Update date: 2026-01-10T07:28:10Z
- Update date including text: 2026-01-10T07:28:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in Senate
- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S820-821)
- Latest action: 2025-02-10: Introduced in Senate

## Actions

- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S820-821)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/502",
    "number": "502",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Rural Hospital Closure Relief Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T07:28:10Z",
    "updateDateIncludingText": "2026-01-10T07:28:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S820-821)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-11T00:07:08Z",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "OK"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "MN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "MS"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "WV"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NM"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MS"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s502is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 502\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2025 Mr. Durbin (for himself, Mr. Lankford , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to restore State authority to waive for certain facilities the 35\u2013mile rule for designating critical access hospitals under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Hospital Closure Relief Act of 2025 .\n#### 2. Restoring State authority to waive the 35\u2013mile rule for certain Medicare critical access hospital designations\n##### (a) In general\nSection 1820 of the Social Security Act ( 42 U.S.C. 1395i\u20134 ) is amended\u2014\n**(1)**\nin subsection (c)(2)\u2014\n**(A)**\nin subparagraph (B)(i)\u2014\n**(i)**\nin subclause (I), by striking or at the end;\n**(ii)**\nin subclause (II), by inserting or at the end; and\n**(iii)**\nby adding at the end the following new subclause:\n(III) subject to subparagraph (G), is a hospital described in subparagraph (F) and is certified, on or after the date of the enactment of the Rural Hospital Closure Relief Act of 2025 , and before the date that is 9 years after the date of enactment of this subclause, by the State as being a necessary provider of health care services to residents in the area; ; and\n**(B)**\nby adding at the end the following new subparagraphs:\n(F) Hospital described For purposes of subparagraph (B)(i)(III), a hospital described in this subparagraph is a hospital that\u2014 (i) is a sole community hospital (as defined in section 1886(d)(5)(D)(iii)), a medicare dependent, small rural hospital (as defined in section 1886(d)(5)(G)(iv)), a low-volume hospital that in 2021 receives a payment adjustment under section 1886(d)(12), or a subsection (d) hospital (as defined in section 1886(d)(1)(B)); (ii) is located in a rural area, as defined in section 1886(d)(2)(D), or a rural census tract of a metropolitan statistical area (as determined under the most recent modification of the Goldsmith Modification, originally published in the Federal Register on February 27, 1992 (57 Fed. Reg. 6725)); (iii) (I) is located\u2014 (aa) in a county that has a percentage of individuals with income at or below the Federal poverty level in 2023 or 2024 that is higher than the national or statewide average in that year; or (bb) in a health professional shortage area (as defined in section 332(a)(1)(A) of the Public Health Service Act); or (II) has a percentage of inpatient days of individuals entitled to benefits under part A of this title in 2023 or 2024 that is higher than the national or statewide average in that year; (iv) has attested to the Secretary that the hospital\u2014 (I) was operating as of the date of enactment of this subparagraph; and (II) had 2 consecutive years of negative operating margins preceding the date of certification described in subparagraph (B)(i)(III), as defined by the Secretary in the regulations or program instruction issued pursuant to section 2(b) of the Rural Hospital Closure Relief Act of 2025 ; and (v) submits to the Secretary, at such time and in such manner as the Secretary may require, an application for certification of the facility as a critical access hospital, including an attestation outlining\u2014 (I) the good governance qualifications and strategic plan for multi-year financial solvency of the hospital; and (II) the hospital\u2019s commitment to open and maintain, for the duration of the hospital\u2019s designation as a critical access hospital under this section, a new service line or expanded service capacity for a service that is in high demand or limited supply in the hospital\u2019s service area (determined based on the hospital\u2019s most recent community health needs assessment under section 501(r)(3) of the Internal Revenue Code of 1986 (or other comparable assessment)), such as obstetrics or behavioral health care services. (G) Limitation on certain designations (i) In general Subject to clauses (ii) and (iii), the Secretary may not under subsection (e) certify pursuant to a certification by a State under subparagraph (B)(i)(III)\u2014 (I) more than a total of 120 facilities as critical access hospitals; and (II) within any one State, more than 5 facilities as critical access hospitals. (ii) Process The Secretary shall follow the following process in carrying out clause (i) with respect to each year in which the Secretary determines that the limitation under clause (i)(I) has not been reached: (I) Initial assessment The Secretary shall conduct an initial assessment of the total number of hospitals described in paragraph (2)(F). (II) Initial allocation Of the total number of designations available under clause (i), the Secretary shall allocate 1 for a hospital in each State that the Secretary determines (based on the initial assessment under subclause (I)) has one or more hospitals described in paragraph (2)(F). (III) Remaining allocation Of the total number of designations available under clause (i), after application of subclause (II), the Secretary shall allocate the remaining number on a proportional basis based on the total number of hospitals described in paragraph (2)(F) in each State that are eligible (as determined based on the initial assessment under subclause (I)). (iii) Sunset Effective beginning on the date that is 9 years after the date of enactment of this subparagraph, the Secretary may not certify a hospital as a critical access hospital pursuant to a certification by a State under subparagraph (B)(i)(III). (H) Information submission requirements for hospitals certified pursuant to Rural Hospital Closure Relief Act (i) In general A critical access hospital that is certified under subsection (e) pursuant to a certification by a State under subparagraph (B)(i)(III) shall submit to the Secretary the following at a time, and in a manner, specified by the Secretary: (I) Reports Reports containing such information as the Secretary may specify with respect to items and services furnished as part of the new service line or expanded service capacity for a service as described in the attestation submitted by the critical access hospital under subparagraph (F)(v)(II). To the extent practicable, the Secretary shall align such reporting with other reporting requirements applicable to critical access hospitals under this subsection. (II) Notice If the critical access hospital materially changes the new service line or expanded capacity for a service as so described, notice of such changes along with a plan to satisfactorily maintain access to care (as determined by the Secretary). (ii) Revocation of certification for noncompliance If the Secretary determines that a critical access hospital described in clause (i) has failed to submit an annual report required under subclause (I) of such clause or a notice required under subclause (II) of such clause, the Secretary may, as the Secretary determines appropriate, revoke the certification of the critical access hospital under subsection (e). ; and\n**(2)**\nin subsection (e), by inserting , subject to subsection (c)(2)(G), after The Secretary shall .\n##### (b) Implementation\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall issue final regulations or program instruction to carry out subsection (a).\n##### (c) Clarification regarding facilities that meet distance or other criteria and application of other criteria\nNothing in this section shall affect\u2014\n**(1)**\nthe application of criteria for designation as a critical access hospital described in subclause (I) or (II) of section 1820(c)(2)(B)(i) of the Social Security Act ( 42 U.S.C. 1395i\u20134(c)(2)(B)(i) ); or\n**(2)**\nthe application of criteria for designation as a critical access hospital described in clauses (ii) through (v) of section 1820(c)(2)(B) of the Social Security Act ( 42 U.S.C. 1395i\u20134(c)(2)(B) ).\n##### (d) GAO study and report\n**(1) Study**\nThe Comptroller General of the United States (in this section referred to as the Comptroller General ) shall conduct a study on the implementation of the amendments made by subsection (a). To the extent such data are available and reliable, such study shall include\u2014\n**(A)**\nan analysis of\u2014\n**(i)**\nthe characteristics of facilities designated as critical access hospitals pursuant to section 1820(c)(2)(B)(i)(III) of the Social Security Act, as added by subsection (a);\n**(ii)**\nan analysis of the financial status and outlook for such facilities based on their designation as a critical access hospital pursuant to such section; and\n**(iii)**\nan analysis of any increase in expenditures under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) as a result of such designation, relative to the expected baseline expenditures under the Medicare program if such facilities had not received such designation; and\n**(B)**\nan assessment of whether the authority to designate facilities as critical access hospitals pursuant to such section 1820(c)(2)(B)(i)(III) promotes access to care in rural areas.\n**(2) Report**\nNot later than 6 years after the date of the enactment of this Act, the Comptroller General shall submit to Congress a report containing the results of the study conducted under subsection (a), together with recommendations for such legislation and administrative action as the Comptroller General determines appropriate.\n#### 3. MedPAC study and report on payment systems for rural hospitals\n##### (a) Study\nThe Medicare Payment Advisory Commission (in this section referred to as the Commission ) shall conduct a study, using data from 2018 through 2028, on payment systems for rural hospitals under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ). Such study shall include an analysis of\u2014\n**(1)**\nfacilities designated as critical access hospitals pursuant to section 1820(c)(2)(B)(i)(III) of the Social Security Act, as added by section 2(a);\n**(2)**\nfeatures of payment systems for rural hospitals, including value-based payment systems, that would\u2014\n**(A)**\nensure financial sustainability for the Medicare program; and\n**(B)**\npreserve access to care for Medicare beneficiaries; and\n**(3)**\nif the Commission recommends any new payment system for rural hospitals under the Medicare program, to the extent feasible, the impacts of transition from existing payment systems to such new payment system.\n##### (b) Report\nNot later than 8 years after the date of enactment of this Act, the Commission shall submit to Congress a report on the study conducted under subsection (a), together with recommendations for such legislation and administrative action as the Commission determines appropriate.\n##### (c) Definition of rural hospital\nIn this section, the term rural hospital means\u2014\n**(1)**\na critical access hospital (as defined in section 1861(mm)(1) of the Social Security Act ( 42 U.S.C. 1395x(mm)(1) ));\n**(2)**\na subsection (d) hospital (as defined in section 1886(d)(1)(B) of the Social Security Act ( 42 U.S.C. 1395ww(d)(1)(B) )) that is located in a rural census tract of a metropolitan statistical area (as determined under the most recent modification of the Goldsmith Modification, originally published in the Federal Register on February 27, 1992 (57 Fed. Reg. 6725));\n**(3)**\na sole community hospital (as defined in section 1886(d)(5)(D)(iii)) of the Social Security Act ( 42 U.S.C. 1395ww(d)(5)(D)(iii) ));\n**(4)**\na medicare dependent, small rural hospital (as defined in section 1886(d)(5)(G)(iv) of the Social Security Act ( 42 U.S.C. 1395ww(d)(5)(G)(iv) )); and\n**(5)**\na low-volume hospital (as defined in section 1886(d)(12)(C)(i) of the Social Security Act ( 42 U.S.C. 1395ww(d)(12)(C)(i) )).\n#### 4. Sunset\nNot later than 9 years after the date of enactment of this Act, the Secretary shall establish a mechanism and provide guidance and technical assistance under which any facility that was designated as a critical access hospital pursuant to a certification by a State under section 1820(c)(2)(B)(i)(III) of the Social Security Act, as added by section 2(a), may transition within 1 year to one of the following payment models:\n**(1)**\nSuch new model or models recommended by the Medicare Payment Advisory Commission in the report submitted under section 3.\n**(2)**\nThe prospective payment model (or models) under which the facility received payment under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) prior to being so designated pursuant to such certification.\n**(3)**\nPayment as a rural emergency hospital under section 1834(x) of the Social Security Act ( 42 U.S.C. 1395m(x) ).",
      "versionDate": "2025-02-10",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6240",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rural Hospital Closure Relief Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-24T16:24:34Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-24T16:24:29Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-04-24T16:24:44Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-04-24T16:24:15Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-04-24T16:24:10Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-04-24T16:24:00Z"
          },
          {
            "name": "Medicare Payment Advisory Commission",
            "updateDate": "2025-04-24T16:24:39Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-04-24T16:24:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T16:57:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119s502",
          "measure-number": "502",
          "measure-type": "s",
          "orig-publish-date": "2025-02-10",
          "originChamber": "SENATE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s502v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rural Hospital Closure Relief Act of </strong><strong>2025</strong></p><p>This bill temporarily allows additional hospitals to qualify as critical access hospitals (CAHs) that receive special payment under Medicare.</p><p>Currently, in order to qualify as a CAH under Medicare, a hospital must either (1) be located more than 35 miles (or 15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area.</p><p>The bill allows\u00a0a hospital to also qualify if the hospital is a small, rural hospital that (1) serves a health professional shortage area, or a high number of low-income individuals or Medicare beneficiaries; (2) has experienced financial losses for two consecutive years; and (3) attests to having a strategic plan to address financial solvency and to committing to provide a service that is in high demand in the hospital's service area. This authority expires nine years after the bill's enactment.</p><p>The Government Accountability Office must study the effects of the bill's implementation. In addition, the Medicare Payment Advisory Commission must study and recommend payment systems for rural hospitals under Medicare.\u00a0The Centers for Medicare & Medicaid Services must subsequently establish a mechanism and issue guidance on how newly designated CAHs may transition to different payment models under Medicare, including any new payment models recommended by the commission.</p>"
        },
        "title": "Rural Hospital Closure Relief Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s502.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Hospital Closure Relief Act of </strong><strong>2025</strong></p><p>This bill temporarily allows additional hospitals to qualify as critical access hospitals (CAHs) that receive special payment under Medicare.</p><p>Currently, in order to qualify as a CAH under Medicare, a hospital must either (1) be located more than 35 miles (or 15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area.</p><p>The bill allows\u00a0a hospital to also qualify if the hospital is a small, rural hospital that (1) serves a health professional shortage area, or a high number of low-income individuals or Medicare beneficiaries; (2) has experienced financial losses for two consecutive years; and (3) attests to having a strategic plan to address financial solvency and to committing to provide a service that is in high demand in the hospital's service area. This authority expires nine years after the bill's enactment.</p><p>The Government Accountability Office must study the effects of the bill's implementation. In addition, the Medicare Payment Advisory Commission must study and recommend payment systems for rural hospitals under Medicare.\u00a0The Centers for Medicare & Medicaid Services must subsequently establish a mechanism and issue guidance on how newly designated CAHs may transition to different payment models under Medicare, including any new payment models recommended by the commission.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s502"
    },
    "title": "Rural Hospital Closure Relief Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Hospital Closure Relief Act of </strong><strong>2025</strong></p><p>This bill temporarily allows additional hospitals to qualify as critical access hospitals (CAHs) that receive special payment under Medicare.</p><p>Currently, in order to qualify as a CAH under Medicare, a hospital must either (1) be located more than 35 miles (or 15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area.</p><p>The bill allows\u00a0a hospital to also qualify if the hospital is a small, rural hospital that (1) serves a health professional shortage area, or a high number of low-income individuals or Medicare beneficiaries; (2) has experienced financial losses for two consecutive years; and (3) attests to having a strategic plan to address financial solvency and to committing to provide a service that is in high demand in the hospital's service area. This authority expires nine years after the bill's enactment.</p><p>The Government Accountability Office must study the effects of the bill's implementation. In addition, the Medicare Payment Advisory Commission must study and recommend payment systems for rural hospitals under Medicare.\u00a0The Centers for Medicare & Medicaid Services must subsequently establish a mechanism and issue guidance on how newly designated CAHs may transition to different payment models under Medicare, including any new payment models recommended by the commission.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s502"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s502is.xml"
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
      "title": "Rural Hospital Closure Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Hospital Closure Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to restore State authority to waive for certain facilities the 35-mile rule for designating critical access hospitals under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:19Z"
    }
  ]
}
```
