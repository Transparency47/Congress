# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7096?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7096
- Title: Ensuring Seniors’ Access to Quality Care Act
- Congress: 119
- Bill type: HR
- Bill number: 7096
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-05-14T08:08:35Z
- Update date including text: 2026-05-14T08:08:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-15 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-15 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7096",
    "number": "7096",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000298",
        "district": "4",
        "firstName": "Ron",
        "fullName": "Rep. Estes, Ron [R-KS-4]",
        "lastName": "Estes",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Ensuring Seniors\u2019 Access to Quality Care Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:35Z",
    "updateDateIncludingText": "2026-05-14T08:08:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-15T14:03:05Z",
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NE"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "VA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "KS"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "OR"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7096ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7096\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Estes (for himself and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to ensure appropriate approval for certain skilled nursing facility and nursing facility nursing aide training and competency evaluation programs under the Medicare and Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Ensuring Seniors\u2019 Access to Quality Care Act .\n#### 2. Ensuring appropriate approval for certain skilled nursing facility and nursing facility nursing aide training and competency evaluation programs under the Medicare and Medicaid program\n##### (a) Medicare\nSection 1819(f)(2) of the Social Security Act ( 42 U.S.C. 1395i\u20133(f)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B)(iii)\u2014\n**(A)**\nin the matter preceding subclause (I), by striking subparagraphs (C) and (D) and inserting subparagraph (C) ; and\n**(B)**\nin subclause (I)\u2014\n**(i)**\nin item (b), by striking or at the end;\n**(ii)**\nby amending item (c) to read as follows:\n(c) has been assessed a civil money penalty described in subsection (h)(2)(B)(ii) or section 1919(h)(2)(A)(ii) of not less than $12,924 and has been cited for a deficiency relating to the quality of care provided to residents of the facility; or ; and\n**(iii)**\nby adding at the end the following new item:\n(d) has been subject to a remedy described in clause (i) or (iii) of subsection (h)(2)(B), subsection (h)(4), section 1919(h)(1)(B)(i), or in clause (i), (iii), or (iv) of section 1919(h)(2)(A), or ; and\n**(2)**\nby striking subparagraph (D).\n##### (b) Medicaid\nSection 1919(f)(2) of the Social Security Act ( 42 U.S.C. 1396r(f)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B)(iii)\u2014\n**(A)**\nin the matter preceding subclause (I), by striking subparagraphs (C) and (D) and inserting subparagraph (C) ; and\n**(B)**\nin subclause (I)\u2014\n**(i)**\nin item (b), by striking or at the end;\n**(ii)**\nby amending item (c) to read as follows:\n(c) has been assessed a civil money penalty described in subsection (h)(2)(A)(ii) or section 1819(h)(2)(B)(ii) of not less than $12,924 and has been cited for a deficiency relating to the quality of care provided to residents of the facility; or ; and\n**(iii)**\nby adding at the end the following new item:\n(d) has been subject to a remedy described in subsection (h)(1)(B)(i), clauses (i), (iii), or (iv) of subsection (h)(2)(A), clauses (i) or (iii) of section 1819(h)(2)(B), or section 1819(h)(4), or ; and\n**(2)**\nby striking subparagraph (D).",
      "versionDate": "2026-01-15",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-02-06T18:38:19Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7096ih.xml"
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
      "title": "Ensuring Seniors\u2019 Access to Quality Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T10:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Seniors\u2019 Access to Quality Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T10:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles XVIII and XIX of the Social Security Act to ensure appropriate approval for certain skilled nursing facility and nursing facility nursing aide training and competency evaluation programs under the Medicare and Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T10:33:16Z"
    }
  ]
}
```
