# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8215?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8215
- Title: Volume II Transparency Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8215
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-04-14T18:33:18Z
- Update date including text: 2026-04-14T18:33:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8215",
    "number": "8215",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Volume II Transparency Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-14T18:33:18Z",
    "updateDateIncludingText": "2026-04-14T18:33:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
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
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:34:15Z",
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
      "bioguideId": "M001245",
      "district": "18",
      "firstName": "Christian",
      "fullName": "Rep. Menefee, Christian D. [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Menefee",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8215ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8215\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Cohen (for himself and Mr. Menefee ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to disclose volume II of the report prepared by Special Counsel Jack Smith.\n#### 1. Short title\nThis Act may be cited as the Volume II Transparency Act of 2026 .\n#### 2. Disclosure of volume II of report prepared by Special Counsel Jack Smith\n##### (a) Requirement\nNotwithstanding any other provision of law, not later than 7 days after the date of the enactment of this Act, the Attorney General shall publish on the internet website of the Department of Justice volume II of the report prepared by Special Counsel Jack Smith.\n##### (b) Redactions\nThe Attorney General may redact\u2014\n**(1)**\nthe name of a witness and any other information that would identify such witness, if such individual did not aid or abet the commission of a criminal offense described in the volume;\n**(2)**\nthe name of a victim and any other information that would identify such victim of a criminal offense described in the volume; and\n**(3)**\nnational security or other information that would negatively impact national security if such information was publicly disclosed.\n##### (c) Public interest\nA redaction made under subsection (b)(3) may be made public if the Attorney General determines that such publication is in the public interest.",
      "versionDate": "2026-04-09",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-14T18:33:18Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8215ih.xml"
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
      "title": "Volume II Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Volume II Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Attorney General to disclose volume II of the report prepared by Special Counsel Jack Smith.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T08:18:23Z"
    }
  ]
}
```
