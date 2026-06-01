# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7665?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7665
- Title: Friends in the Field Act
- Congress: 119
- Bill type: HR
- Bill number: 7665
- Origin chamber: House
- Introduced date: 2026-02-24
- Update date: 2026-03-09T18:26:32Z
- Update date including text: 2026-03-09T18:26:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-24: Introduced in House

## Actions

- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7665",
    "number": "7665",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Friends in the Field Act",
    "type": "HR",
    "updateDate": "2026-03-09T18:26:32Z",
    "updateDateIncludingText": "2026-03-09T18:26:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-24",
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
          "date": "2026-02-24T15:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7665ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7665\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2026 Ms. Scholten introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to add biological pest control to the list of high-priority research and extension areas.\n#### 1. Short title\nThis Act may be cited as the Friends in the Field Act .\n#### 2. Addition of biological pest control to high-priority research and extension areas\nSection 1672(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925(d) ) is amended by adding at the end the following:\n(21) Biological pest control Research and extension grants may be made under this section for the purposes of supporting research, development, or education materials, information, and outreach programs regarding biological pest control to limit crop damage and food-borne illnesses. .",
      "versionDate": "2026-02-24",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-09T18:26:32Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7665ih.xml"
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
      "title": "Friends in the Field Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Friends in the Field Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Agriculture, Conservation, and Trade Act of 1990 to add biological pest control to the list of high-priority research and extension areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T09:18:28Z"
    }
  ]
}
```
