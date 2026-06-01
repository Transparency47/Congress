# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8174?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8174
- Title: To amend title 31, United States Code, to prohibit the issuance of United States currency and securities containing the signature of the sitting President.
- Congress: 119
- Bill type: HR
- Bill number: 8174
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-04-09T14:49:37Z
- Update date including text: 2026-04-09T14:49:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8174",
    "number": "8174",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000585",
        "district": "34",
        "firstName": "Jimmy",
        "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
        "lastName": "Gomez",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To amend title 31, United States Code, to prohibit the issuance of United States currency and securities containing the signature of the sitting President.",
    "type": "HR",
    "updateDate": "2026-04-09T14:49:37Z",
    "updateDateIncludingText": "2026-04-09T14:49:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
          "date": "2026-04-02T12:32:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8174ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8174\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Mr. Gomez introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend title 31, United States Code, to prohibit the issuance of United States currency and securities containing the signature of the sitting President.\n#### 1. Prohibiting the President\u2019s signature from appearing on United States currency or securities\n##### (a) In general\nSection 5114(b) of title 31, United States Code, is amended by adding at the end the following: United States currency or securities containing the signature of an individual may not be issued during any period in which such individual is serving as President. .\n##### (b) Explicit statutory waiver\nThe prohibition contained in the amendment made by subsection (a) may only be waived by the enactment, after the date of the enactment of this section, of specific statutory authorization for such activity that explicitly waives the application of such prohibition by reference.",
      "versionDate": "2026-04-02",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-09T14:49:36Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8174ih.xml"
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
      "title": "To amend title 31, United States Code, to prohibit the issuance of United States currency and securities containing the signature of the sitting President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T08:18:39Z"
    },
    {
      "title": "To amend title 31, United States Code, to prohibit the issuance of United States currency and securities containing the signature of the sitting President.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T08:05:49Z"
    }
  ]
}
```
