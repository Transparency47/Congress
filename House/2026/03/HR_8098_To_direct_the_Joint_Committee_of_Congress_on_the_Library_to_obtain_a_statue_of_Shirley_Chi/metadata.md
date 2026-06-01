# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8098?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8098
- Title: To direct the Joint Committee of Congress on the Library to obtain a statue of Shirley Chisholm for placement in the United States Capitol.
- Congress: 119
- Bill type: HR
- Bill number: 8098
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-02T18:22:34Z
- Update date including text: 2026-04-02T18:22:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8098",
    "number": "8098",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001067",
        "district": "9",
        "firstName": "Yvette",
        "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
        "lastName": "Clarke",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To direct the Joint Committee of Congress on the Library to obtain a statue of Shirley Chisholm for placement in the United States Capitol.",
    "type": "HR",
    "updateDate": "2026-04-02T18:22:34Z",
    "updateDateIncludingText": "2026-04-02T18:22:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8098ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8098\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Ms. Clarke of New York introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo direct the Joint Committee of Congress on the Library to obtain a statue of Shirley Chisholm for placement in the United States Capitol.\n#### 1. Placement of statue of Shirley Chisholm in United States Capitol\n##### (a) Obtaining Statue\nNot later than 2 years after the date of the enactment of this Act, the Joint Committee of Congress on the Library shall enter into an agreement to obtain a statue of Shirley Chisholm, under such terms and conditions as the Joint Committee considers appropriate consistent with applicable law. The Joint Committee may authorize the Architect of the Capitol to enter into the agreement and related contracts required under this subsection on its behalf, under such terms and conditions as the Joint Committee may require.\n##### (b) Placement\nThe Joint Committee of Congress on the Library shall place the statue obtained under subsection (a) in a public permanent location in the United States Capitol.\n##### (c) Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this Act, and any amounts so appropriated shall remain available until expended.",
      "versionDate": "2026-03-26",
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
        "name": "Congress",
        "updateDate": "2026-04-02T18:22:34Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8098ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Joint Committee of Congress on the Library to obtain a statue of Shirley Chisholm for placement in the United States Capitol.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-01T07:03:19Z"
    },
    {
      "title": "To direct the Joint Committee of Congress on the Library to obtain a statue of Shirley Chisholm for placement in the United States Capitol.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T08:06:48Z"
    }
  ]
}
```
