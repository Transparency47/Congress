# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8001?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8001
- Title: First Responders’ Equipment Access Act
- Congress: 119
- Bill type: HR
- Bill number: 8001
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-03T14:51:48Z
- Update date including text: 2026-04-03T14:51:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8001",
    "number": "8001",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "C001039",
        "district": "3",
        "firstName": "Kat",
        "fullName": "Rep. Cammack, Kat [R-FL-3]",
        "lastName": "Cammack",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "First Responders\u2019 Equipment Access Act",
    "type": "HR",
    "updateDate": "2026-04-03T14:51:48Z",
    "updateDateIncludingText": "2026-04-03T14:51:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8001ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8001\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mrs. Cammack introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Administrator of the Environmental Protection Agency to amend regulations relating to exemptions for engines and equipment for purposes of national security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the First Responders\u2019 Equipment Access Act .\n#### 2. Amendment to regulations exempting engines/equipment for national security\nNot later than 90 days after the date of enactment of this Act, the Administrator of the Environmental Protection Agency shall revise the regulations under section 1068.225(d) of title 40, Code of Federal Regulations (as in effect on the date of enactment of this Act)\u2014\n**(1)**\nto authorize\u2014\n**(A)**\nmanufacturers and secondary engine manufacturers to request a national security exemption under such section 1068.225(d) for engines or equipment intended to be used by Federal, State, or local agencies for providing law enforcement, disaster relief, search and rescue, fire response, or emergency medical services; and\n**(B)**\nan agency of the Federal Government responsible for national defense and the Department of Homeland Security (including the Federal Emergency Management Agency) to endorse a request described in subparagraph (A); and\n**(2)**\nto specify that a request for a national security exemption described in paragraph (1)(A), and an endorsement of such a request described in paragraph (1)(B), is not required to specify a quantity of engines or equipment to be exempted in order to receive such an exemption.",
      "versionDate": "2026-03-19",
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
        "name": "Emergency Management",
        "updateDate": "2026-04-03T14:51:48Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8001ih.xml"
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
      "title": "First Responders\u2019 Equipment Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "First Responders\u2019 Equipment Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Environmental Protection Agency to amend regulations relating to exemptions for engines and equipment for purposes of national security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:30Z"
    }
  ]
}
```
