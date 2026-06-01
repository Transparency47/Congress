# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1234?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1234
- Title: Supporting the mission and goals of National Fentanyl Awareness Day in 2026, including increasing individual and public awareness of the impact of fake or counterfeit fentanyl pills on families and young people.
- Congress: 119
- Bill type: HRES
- Bill number: 1234
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-18T17:31:08Z
- Update date including text: 2026-05-18T17:31:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-29 - IntroReferral: Submitted in House
- Latest action: 2026-04-29: Submitted in House

## Actions

- 2026-04-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1234",
    "number": "1234",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000620",
        "district": "7",
        "firstName": "Brittany",
        "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
        "lastName": "Pettersen",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Supporting the mission and goals of National Fentanyl Awareness Day in 2026, including increasing individual and public awareness of the impact of fake or counterfeit fentanyl pills on families and young people.",
    "type": "HRES",
    "updateDate": "2026-05-18T17:31:08Z",
    "updateDateIncludingText": "2026-05-18T17:31:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
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
          "date": "2026-04-29T13:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-29T13:03:10Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "PA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1234ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1234\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Ms. Pettersen (for herself, Mr. Fitzpatrick , Mrs. Trahan , Mr. Neguse , and Mr. McDowell ) submitted the following resolution; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nSupporting the mission and goals of National Fentanyl Awareness Day in 2026, including increasing individual and public awareness of the impact of fake or counterfeit fentanyl pills on families and young people.\nThat the House of Representatives\u2014\n**(1)**\nsupports the recognition and goals of National Fentanyl Awareness Day, which include increasing individual and public awareness of the impact of fake or counterfeit fentanyl pills on families and young people;\n**(2)**\napplauds the work of Federal, State, and local law enforcement agencies that work to combat the proliferation of counterfeit pills;\n**(3)**\nencourages the use of existing authorities to proactively stop and prevent the spread of illicit counterfeit pills; and\n**(4)**\nsupports the designation of National Fentanyl Awareness Day .",
      "versionDate": "2026-04-29",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-29",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2109; text: CR S2135-2136)"
      },
      "number": "704",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution supporting the mission and goals of National Fentanyl Awareness Day in 2026, including increasing individual and public awareness of the impact of fake or counterfeit fentanyl pills on families and young people.",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-29",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "359",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting the mission and goals of National Fentanyl Awareness Day in 2025, including increasing individual and public awareness of the impact of fake or counterfeit fentanyl pills on families and young people.",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-29",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2643; text: CR S2669)"
      },
      "number": "186",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution supporting the mission and goals of National Fentanyl Awareness Day in 2025, including increasing individual and public awareness of the impact of fake or counterfeit fentanyl pills on families and young people.",
      "type": "SRES"
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
        "name": "Health",
        "updateDate": "2026-05-14T18:55:16Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1234ih.xml"
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
      "title": "Supporting the mission and goals of National Fentanyl Awareness Day in 2026, including increasing individual and public awareness of the impact of fake or counterfeit fentanyl pills on families and young people.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T09:48:52Z"
    },
    {
      "title": "Supporting the mission and goals of National Fentanyl Awareness Day in 2026, including increasing individual and public awareness of the impact of fake or counterfeit fentanyl pills on families and young people.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T08:06:29Z"
    }
  ]
}
```
