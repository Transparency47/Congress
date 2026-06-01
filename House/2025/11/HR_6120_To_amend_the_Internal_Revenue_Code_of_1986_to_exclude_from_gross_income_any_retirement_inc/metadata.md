# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6120?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6120
- Title: SROS Act
- Congress: 119
- Bill type: HR
- Bill number: 6120
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-01-10T07:29:26Z
- Update date including text: 2026-01-10T07:29:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6120",
    "number": "6120",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "Z000018",
        "district": "1",
        "firstName": "Ryan",
        "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
        "lastName": "Zinke",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "SROS Act",
    "type": "HR",
    "updateDate": "2026-01-10T07:29:26Z",
    "updateDateIncludingText": "2026-01-10T07:29:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-11-18T15:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "PA"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "AZ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "MN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6120ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6120\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Zinke (for himself, Mr. Davis of North Carolina , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income any retirement income received by individuals who retired from service as a law enforcement officer or member of the Armed Forces and subsequently serve as school resource officers.\n#### 1. Short title\nThis Act may be cited as the Strengthening Resources for our Schools Act or the SROS Act .\n#### 2. Exclusion from gross income of retirement income received by school resource officers\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986, as amended by section 70435(a) of Public Law 119\u201321 , is amended by inserting after section 139L the following new section:\n139M. Retirement income received by school resource officers (a) In general Subject to subsection (e), in the case of an individual described in subsection (b) who is employed as a school resource officer during a taxable year, with respect to any period in such taxable year in which such individual is so employed, gross income shall not include any retirement income received by such individual during such period. (b) Requirements An individual is described in this subsection if such individual\u2014 (1) has retired from employment as\u2014 (A) a member of the Armed Forces of the United States, or (B) a law enforcement officer (as defined in section 2503 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10533 )), (2) is employed as a school resource officer after having successfully cleared any background check required for such employment, and (3) is in compliance with all applicable requirements of the peace officer standards and training agency of the State in which such individual is employed as a school resource officer. (c) Retirement income For purposes of this section, the term retirement income means any otherwise includible income, distribution, or payment received by an individual from any pension, annuity, retirement income account, defined contribution plan, or defined benefit plan which is associated with employment described in subsection (b)(1). (d) Other definitions In this section\u2014 (1) Peace officer standards and training agency The term peace officer standards and training agency means an agency of a State with the statutory authority under State law to set standards for the hiring, training, ethical conduct, and retention of the law enforcement officers of the State through certification, licensing, or other similar qualification process. (2) School resource officer The term school resource officer has the same meaning given such term under section 1709 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10389 ). (e) Lifetime exemption In the case of an individual described in subsection (b) who has been employed as a school resource officer for a period of not less than 10 years, in addition to any period described in subsection (a), gross income shall not include any retirement income received by such individual during any period after such employment has ended. (f) Regulations and guidance Not later than 180 days after the date of enactment of this section, the Secretary shall prescribe such regulations or other guidance as may be necessary to carry out the purposes of this section. .\n##### (b) Information reporting\n**(1) In general**\nSubpart A of part III of subchapter A of chapter 61 of the Internal Revenue Code of 1986, as amended by section 70421(d) of Public Law 119\u201321 , is amended by inserting after section 6039L the following new section:\n6039M. Information with respect to school resource officers The head of any law enforcement agency employing an individual described in section 139M(b) shall provide the Secretary with notice (in such manner as the Secretary may prescribe) regarding\u2014 (1) the initial date that such individual began employment as a school resource officer, and (2) the date on which the employment of such individual as a school resource officer has ended. .\n**(2) Penalties**\nSection 6724(d)(1) of such Code is amended by striking and at the end of subparagraph (C), by striking the period at the end of subparagraph (D) and inserting , and , and by inserting after subparagraph (D) the following new subparagraph:\n(E) any notice required to be filed under section 6039M. .\n##### (c) Clerical amendments\n**(1)**\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986, as amended by section 70435(b) of Public Law 119\u201321 , is amended by inserting after the item relating to section 139L the following new item:\nSec. 139M. Retirement income received by school resource officers. .\n**(2)**\nThe table of sections for subpart A of part III of subchapter A of chapter 61 of such Code, as amended by section 70421(d) of Public Law 119\u201321 , is amended by inserting after the item relating to section 6039L the following new item:\nSec. 6039M. Information with respect to school resource officers. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of enactment of this Act.",
      "versionDate": "2025-11-18",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-11-18",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3189",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SROS Act",
      "type": "S"
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
        "name": "Taxation",
        "updateDate": "2025-11-19T16:32:36Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6120ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SROS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T10:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SROS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-19T10:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Resources for our Schools Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-19T10:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude from gross income any retirement income received by individuals who retired from service as a law enforcement officer or member of the Armed Forces and subsequently serve as school resource officers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-19T10:03:22Z"
    }
  ]
}
```
