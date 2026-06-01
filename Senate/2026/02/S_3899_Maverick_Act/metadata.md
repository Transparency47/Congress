# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3899?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3899
- Title: Maverick Act
- Congress: 119
- Bill type: S
- Bill number: 3899
- Origin chamber: Senate
- Introduced date: 2026-02-24
- Update date: 2026-03-13T22:30:38Z
- Update date including text: 2026-03-13T22:30:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in Senate
- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2026-02-24: Introduced in Senate

## Actions

- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Armed Services.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3899",
    "number": "3899",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Maverick Act",
    "type": "S",
    "updateDate": "2026-03-13T22:30:38Z",
    "updateDateIncludingText": "2026-03-13T22:30:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-24",
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
          "date": "2026-02-24T20:51:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3899is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3899\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2026 Mr. Sheehy (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo authorize the transfer by the Secretary of the Navy to the U.S. Space and Rocket Center Commission in Huntsville, Alabama, of certain F\u201314 Tomcat aircraft.\n#### 1. Short title\nThis Act may be cited as the Maverick Act .\n#### 2. Conveyance of certain aircraft from the Navy to the U.S. Space and Rocket Center Commission in Huntsville, Alabama\n##### (a) Authority\nThe Secretary of the Navy (in this section referred to as the Secretary ) may transfer (by sale, gift, or otherwise, including by loan) to the U.S. Space and Rocket Center Commission in Huntsville, Alabama (in this section referred to as the Commission ), all right, title, and interest of the United States in one or more F\u201314 Tomcat aircraft currently in the custody of the Department of the Navy or the Department of Defense, on such terms and conditions as the Secretary considers appropriate, which may include requirements for demilitarization and indemnification and may restrict further disposition or use.\n##### (b) Agreements for restoration and operation\nThe Secretary may authorize the Commission to enter into agreements with qualified nonprofit organizations for the purpose of restoring and operating aircraft transferred under subsection (a) for public display, airshows, and commemorative events to preserve naval aviation heritage.\n##### (c) Conveyance at no cost to the United States\nThe conveyance of an aircraft under subsection (a) shall be made at no cost to the United States. Any costs associated with such conveyance, costs of determining compliance with terms of the conveyance, and costs of operation and maintenance of the aircraft conveyed shall be borne by the Commission.",
      "versionDate": "2026-02-24",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-13T22:30:38Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3899is.xml"
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
      "title": "Maverick Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Maverick Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the transfer by the Secretary of the Navy to the U.S. Space and Rocket Center Commission in Huntsville, Alabama, of certain F-14 Tomcat aircraft.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:39Z"
    }
  ]
}
```
