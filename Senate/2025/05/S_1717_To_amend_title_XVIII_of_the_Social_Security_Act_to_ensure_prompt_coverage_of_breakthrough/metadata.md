# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1717?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1717
- Title: Ensuring Patient Access to Critical Breakthrough Products Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1717
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2025-11-11T12:03:14Z
- Update date including text: 2025-11-11T12:03:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-12",
    "latestAction": {
      "actionDate": "2025-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1717",
    "number": "1717",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Ensuring Patient Access to Critical Breakthrough Products Act of 2025",
    "type": "S",
    "updateDate": "2025-11-11T12:03:14Z",
    "updateDateIncludingText": "2025-11-11T12:03:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
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
      "actionDate": "2025-05-12",
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
          "date": "2025-05-12T22:04:49Z",
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
      "sponsorshipDate": "2025-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "WY"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1717is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1717\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Mr. Young (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to ensure prompt coverage of breakthrough devices under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Patient Access to Critical Breakthrough Products Act of 2025 .\n#### 2. Ensuring prompt coverage of breakthrough devices under the Medicare program\n##### (a) Ensuring coverage through a transitional coverage period\n**(1) In general**\nSection 1862(a)(1) of the Social Security Act ( 42 U.S.C. 1395y(a)(1) ) is amended\u2014\n**(A)**\nin subparagraph (O), by striking and at the end;\n**(B)**\nin subparagraph (P), by striking the semicolon at the end and inserting , and ; and\n**(C)**\nby inserting after subparagraph (P) the following new subparagraph:\n(Q) in the case of a breakthrough device (as defined in section 1861(nnn)) furnished during the transitional coverage period (as so defined) with respect to such device, which is not furnished in accordance with the Food and Drug Administration-approved labeling for such device or that the Secretary determines, based on a review of clinical data, presents an undue risk of harm that outweighs the potential clinical benefits for individuals entitled to benefits under part A or enrolled under part B; .\n**(2) Definitions**\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended by adding at the end the following new subsection:\n(nnn) Breakthrough device (1) In general The term breakthrough device means a device so designated by the Secretary under section 1899C. (2) Transitional coverage period The term transitional coverage period means, with respect to a breakthrough device, the 4-year period that begins on the date that such device is so designated by the Secretary under section 1899C. .\n**(3) Breakthrough device determinations**\nPart E of title XVIII of the Social Security Act ( 42 U.S.C. 1395x et seq. ) is amended by adding at the end the following new section:\n1899C. Designation of breakthrough devices (a) In general Beginning 18 months after the date of the enactment of this section, upon application of a manufacturer of a device (as defined in section 201 of the Federal Food, Drug, and Cosmetic Act) that is cleared, classified, or approved under section 510(k), 513(f)(2), or 515 of such Act on or after the date of the enactment of this section, the Secretary shall designate such device as a breakthrough device if the Secretary determines that such device meets the criteria specified in subsection (b). (b) Criteria For purposes of subsection (a), the criteria specified in this subsection is, with respect to a device, that the device is provided with priority review pursuant to section 515B of the Federal Food, Drug, and Cosmetic Act. (c) Determination process (1) In general The Secretary shall make a determination with respect to a device that is the subject of an application described in subsection (a) not later than 6 months after such application is submitted to the Secretary. (2) Explanation required in case of determination that device does not meet criteria for designation In the case that the Secretary determines that a device that is the subject of an application described in subsection (a) does not meet the criteria specified in subsection (b), the Secretary shall notify the manufacturer of such device of such determination and include in such notification an explanation identifying the specific criterion or criteria that such device failed to meet. (d) Reports The Secretary shall submit to Congress on an annual basis a report specifying\u2014 (1) the number of applications received under this section during such year; (2) the number of devices designated as breakthrough devices under this section during such year; and (3) the number of applications for a designation for a device under this section with respect to which the Secretary determined that such device did not meet the criteria specified in subsection (b) during such year. .\n##### (b) Ensuring issuance of national coverage determination during transition period\nSection 1862(l)(2) of the Social Security Act ( 42 U.S.C. 1395y(l)(2) ) is amended by adding at the end the following new flush sentence:\nIn the case of a request for a national coverage determination with respect to a breakthrough device (as defined in section 1861(nnn)), the Secretary shall ensure that a final decision is made on such request prior to the end of the transitional coverage period (as so defined) for such device if such request was submitted to the Secretary before the date that is 9 months (or 12 months, in the case such request is a request to which subparagraph (B) applies) before the last day of such period. .\n##### (c) Funding\nIn addition to amounts otherwise available, there are appropriated to the Centers for Medicare & Medicaid Services Program Management Account, out of any monies in the Treasury not otherwise appropriated, $10,000,000 for each of fiscal years 2026 through 2031, to remain available until expended, to carry out the amendments made by this section.",
      "versionDate": "2025-05-12",
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
        "updateDate": "2025-05-28T13:03:40Z"
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
      "date": "2025-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1717is.xml"
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
      "title": "Ensuring Patient Access to Critical Breakthrough Products Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Patient Access to Critical Breakthrough Products Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to ensure prompt coverage of breakthrough devices under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-23T02:48:18Z"
    }
  ]
}
```
