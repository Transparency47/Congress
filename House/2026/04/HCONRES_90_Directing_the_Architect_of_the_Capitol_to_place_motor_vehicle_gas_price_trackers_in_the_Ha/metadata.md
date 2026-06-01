# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/90?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/90
- Title: Directing the Architect of the Capitol to place motor vehicle gas price trackers in the Hall of the House of Representatives and the Chamber of the Senate.
- Congress: 119
- Bill type: HCONRES
- Bill number: 90
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-01T18:29:44Z
- Update date including text: 2026-05-01T18:29:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-04-23 - IntroReferral: Submitted in House
- Latest action: 2026-04-23: Submitted in House

## Actions

- 2026-04-23 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-04-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/90",
    "number": "90",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Directing the Architect of the Capitol to place motor vehicle gas price trackers in the Hall of the House of Representatives and the Chamber of the Senate.",
    "type": "HCONRES",
    "updateDate": "2026-05-01T18:29:44Z",
    "updateDateIncludingText": "2026-05-01T18:29:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionCode": "1025",
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-04-23T13:01:10Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres90ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 90\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Ms. Stevens submitted the following concurrent resolution; which was referred to the Committee on House Administration\nCONCURRENT RESOLUTION\nDirecting the Architect of the Capitol to place motor vehicle gas price trackers in the Hall of the House of Representatives and the Chamber of the Senate.\n#### 1. Placement of motor vehicle gas price tracker\n##### (a) Locations\nThe Architect of the Capitol shall design, construct, and maintain a motor vehicle gas price tracker, which shall be adjusted on a continuous basis to reflect the average cost of a gallon of regular gasoline in each State and Territory of the United States, in each of the Hall of the House of Representatives and the Chamber of the Senate.\n##### (b) No appropriated funds\nNo appropriated Federal funds may be used for the design, construction, or maintenance of a tracker specified in subsection (a).\n##### (c) Gifts and bequests\nThe Architect of the Capitol may accept, use, and dispose of gifts and bequests of money from individuals for the purposes of this section.\n##### (d) Report\nThe Architect of the Capitol shall submit to the Speaker and the minority leader of the House of Representatives and the majority and minority leaders of the Senate an annual report that contains an accounting of the acceptance, use, and disposition of gifts and bequests of money under this section, including an accounting of the amounts of money accepted and used under this section and the sources of such money.",
      "versionDate": "2026-04-23",
      "versionType": "IH"
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
        "updateDate": "2026-05-01T18:29:43Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres90ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Directing the Architect of the Capitol to place motor vehicle gas price trackers in the Hall of the House of Representatives and the Chamber of the Senate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-25T04:33:35Z"
    },
    {
      "title": "Directing the Architect of the Capitol to place motor vehicle gas price trackers in the Hall of the House of Representatives and the Chamber of the Senate.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T08:07:07Z"
    }
  ]
}
```
