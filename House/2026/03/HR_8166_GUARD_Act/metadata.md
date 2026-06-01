# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8166?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8166
- Title: GUARD Act
- Congress: 119
- Bill type: HR
- Bill number: 8166
- Origin chamber: House
- Introduced date: 2026-03-30
- Update date: 2026-04-14T01:35:50Z
- Update date including text: 2026-04-14T01:35:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-30: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-30: Introduced in House

## Actions

- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-30",
    "latestAction": {
      "actionDate": "2026-03-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8166",
    "number": "8166",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "GUARD Act",
    "type": "HR",
    "updateDate": "2026-04-14T01:35:50Z",
    "updateDateIncludingText": "2026-04-14T01:35:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-30",
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
      "actionDate": "2026-03-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-30",
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
          "date": "2026-03-30T16:02:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8166ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8166\nIN THE HOUSE OF REPRESENTATIVES\nMarch 30, 2026 Mr. Self introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny tax-exempt status to certain organizations receiving contributions or gifts from citizens or nationals of foreign adversaries.\n#### 1. Short title\nThis Act may be cited as the Guarding U.S. Associations from Rogue Donations Act or the GUARD Act .\n#### 2. Denial of tax-exempt status to certain organizations receiving contributions or gifts from citizens or nationals of foreign adversaries\n##### (a) In general\nSection 501 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(s) Denial of tax-Exempt status to certain organizations receiving contributions or gifts from citizens or nationals of foreign adversaries (1) In general Any organization described in paragraph (3) or (4) of subsection (c) which receives any contribution or gift (within the meaning of section 6033(b)(5)) from any individual who is a citizen or national of a foreign adversary shall not be exempt from taxation under subsection (a) for any taxable year ending on or after the date of the receipt of such contribution or gift. (2) Foreign adversary For purposes of paragraph (1), the term foreign adversary means\u2014 (A) the People\u2019s Republic of China, including the Hong Kong and Macau Special Administrative Regions, (B) the Republic of Cuba, (C) the Islamic Republic of Iran, (D) the Democratic People\u2019s Republic of Korea, (E) the Russian Federation, and (F) such other foreign country as the Secretary, in consultation with the Secretary of State, determines is in the national security interest of the United States. .\n##### (b) Effective date\nThe amendment made by this section shall apply with respect to contributions or gifts received after the date of the enactment of this Act.",
      "versionDate": "2026-03-30",
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
        "updateDate": "2026-04-14T01:35:50Z"
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
      "date": "2026-03-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8166ih.xml"
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
      "title": "GUARD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guarding U.S. Associations from Rogue Donations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to deny tax-exempt status to certain organizations receiving contributions or gifts from citizens or nationals of foreign adversaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:40Z"
    }
  ]
}
```
