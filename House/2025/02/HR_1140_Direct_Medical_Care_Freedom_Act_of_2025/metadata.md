# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1140?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1140
- Title: Direct Medical Care Freedom Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1140
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2025-05-06T12:42:02Z
- Update date including text: 2025-05-06T12:42:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1140",
    "number": "1140",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Direct Medical Care Freedom Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-06T12:42:02Z",
    "updateDateIncludingText": "2025-05-06T12:42:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:01:25Z",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "AZ"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "AL"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1140ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1140\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Roy (for himself, Mr. Biggs of Arizona , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow individuals with direct medical care service arrangement to remain eligible individuals for purposes of health savings accounts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Direct Medical Care Freedom Act of 2025 .\n#### 2. Treatment of direct medical care service arrangements\n##### (a) In general\nSection 223(c)(1) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(E) Treatment of direct medical care service arrangements (i) In general A direct medical care service arrangement shall not be treated as a health plan for purposes of subparagraph (A)(ii). (ii) Direct medical care service arrangement For purposes of this paragraph\u2014 (I) In general The term direct medical care service arrangement means, with respect to any individual, an arrangement under which such individual is provided medical care provided by medical care practitioners if the sole compensation for such care is a fixed periodic fee. (II) Application to primary care, specialty care, etc An arrangement shall not fail to be treated as a direct medical care service arrangement merely because such arrangement is restricted to any subset of medical care or medical care practitioners. (iii) Medical care practitioner For purposes of this paragraph, the term medical care practitioner means an individual who is\u2014 (I) a physician (as defined in section 1861(r)(1) of the Social Security Act), or (II) a nurse practitioner, clinical nurse specialist, or physician assistant (as such terms are defined in section 1861(aa)(5) of the Social Security Act). (iv) Medical care For purposes of this paragraph, the term medical care has the meaning given such term in section 213(d)). .\n##### (b) Direct medical care service arrangement fees treated as medical expenses\nSection 223(d)(2)(C) of such Code is amended by striking or at the end of clause (iii), by striking the period at the end of clause (iv) and inserting , or , and by adding at the end the following new clause:\n(v) any direct medical care service arrangement. .\n##### (c) Reporting of direct medical care service arrangement fees on W\u20132\nSection 6051(a) of such Code is amended by striking and at the end of paragraph (16), by striking the period at the end of paragraph (17) and inserting , and , and by inserting after paragraph (17) the following new paragraph:\n(18) in the case of a direct medical care service arrangement (as defined in section 223(c)(1)(E)(ii)) which is provided in connection with employment, the aggregate fees for such arrangement for such employee. .\n##### (d) Effective date\nThe amendments made by this section shall apply to months beginning after December 31, 2024, in taxable years ending after such date.",
      "versionDate": "2025-02-07",
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
        "name": "Taxation",
        "updateDate": "2025-05-06T12:42:02Z"
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
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1140ih.xml"
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
      "title": "Direct Medical Care Freedom Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-10T12:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Direct Medical Care Freedom Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow individuals with direct medical care service arrangement to remain eligible individuals for purposes of health savings accounts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:33:30Z"
    }
  ]
}
```
