# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9076?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9076
- Title: Postal Data Privacy Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 9076
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:23:28Z
- Update date including text: 2026-05-30T09:28:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-29",
    "latestAction": {
      "actionDate": "2026-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9076",
    "number": "9076",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001205",
        "district": "5",
        "firstName": "Mary Gay",
        "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
        "lastName": "Scanlon",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Postal Data Privacy Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-30T08:23:28Z",
    "updateDateIncludingText": "2026-05-30T09:28:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-29",
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
          "date": "2026-05-29T16:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "GA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "MA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "DC"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr9076ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 9076\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2026 Ms. Scanlon (for herself, Mr. Johnson of Georgia , Mr. McGovern , Ms. Norton , and Ms. Jacobs ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require a court order for use of a mail cover.\n#### 1. Short title\nThis Act may be cited as the Postal Data Privacy Act of 2026 .\n#### 2. Mail covers\n##### (a) In general\nChapter 83 of title 18, United States Code, is amended by inserting after section 1737 the following:\n1738. Limitation on use of mail covers (a) Requirement for Court Order (1) Limitation A governmental entity may not use a mail cover, unless the governmental entity obtains a court order pursuant to paragraph (2). (2) Court order A court order authorizing the use of a mail cover may be issued by any court that is a court of competent jurisdiction and shall issue only if a governmental entity offers specific and articulable facts showing that there are reasonable grounds to believe that mail covers are relevant and material to an ongoing criminal investigation. In the case of a State governmental authority, such a court order shall not issue if prohibited by the law of such State. (b) Requirement To Preserve Evidence (1) In general The Chief Postal Inspector, upon the request of a governmental entity, shall take all necessary steps to preserve records and other evidence in its possession pending the issuance of a court order or other process. (2) Period of retention Records referred to in paragraph (1) shall be retained for a period of 90 days, which shall be extended for an additional 90-day period upon a renewed request by the governmental entity. (c) Mail cover defined The term mail cover has the meaning given that term in section 233.3 of title 39, Code of Federal Regulations (or any successor regulation). .\n##### (b) Clerical amendment\nThe table of sections for chapter 83 of title 18, United States Code, is amended by inserting after the item related to section 1737 the following:\n1738. Limitation on use of mail covers. .",
      "versionDate": "2026-05-29",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr9076ih.xml"
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
      "title": "Postal Data Privacy Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Postal Data Privacy Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a court order for use of a mail cover.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:18:30Z"
    }
  ]
}
```
