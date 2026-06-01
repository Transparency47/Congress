# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/61?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/61
- Title: A resolution expressing support for the continued value of arms control agreements and negotiated constraints on Russian and Chinese strategic nuclear forces.
- Congress: 119
- Bill type: SRES
- Bill number: 61
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2026-02-26T11:56:32Z
- Update date including text: 2026-02-26T11:56:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S673-674)
- 2025-02-05 - IntroReferral: Submitted in Senate
- Latest action: 2025-02-05: Submitted in Senate

## Actions

- 2025-02-05 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S673-674)
- 2025-02-05 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/61",
    "number": "61",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A resolution expressing support for the continued value of arms control agreements and negotiated constraints on Russian and Chinese strategic nuclear forces.",
    "type": "SRES",
    "updateDate": "2026-02-26T11:56:32Z",
    "updateDateIncludingText": "2026-02-26T11:56:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S673-674)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
        "item": [
          {
            "date": "2025-02-06T00:10:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-06T00:10:58Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "MD"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "AZ"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NJ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "AZ"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "IL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "DE"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "RI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "WA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "WI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-02-09",
      "state": "VT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CO"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres61is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 61\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Markey submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing support for the continued value of arms control agreements and negotiated constraints on Russian and Chinese strategic nuclear forces.\nThat the Senate\u2014\n**(1)**\ncondemns in the strongest terms the use of nuclear escalatory rhetoric and veiled threats to potentially use nuclear weapons in the context of the illegal invasion of a free and independent Ukraine;\n**(2)**\ncondemns the Russian Federation\u2019s purported suspension of its participation in the New START Treaty;\n**(3)**\ncalls for immediate cessation of nuclear saber rattling and nuclear escalatory rhetoric from the Russian Federation, or by any other nuclear-armed state;\n**(4)**\nemphasizes the continued value of arms control agreements between the United States and the Russian Federation, which possess the world\u2019s largest nuclear arsenals;\n**(5)**\ncalls for the Russian Federation to promptly return to full implementation of the New START Treaty, including onsite inspections, provision of treaty-mandated notifications and data, and resumption of Bilateral Consultative Commission meetings;\n**(6)**\ncalls on the administration to continue to actively pursue a dialogue with the Russian Federation on a new nuclear arms control framework and on risk reduction in order to maintain strategic stability, ensure the conflict in Ukraine does not escalate to nuclear use, and avoid an unrestrained nuclear arms race following the expiration of the New START Treaty;\n**(7)**\ncalls upon the United States and the Russian Federation to continue to respect the numerical constraints on the strategic deployed nuclear forces established by the New START Treaty until such time as a new nuclear arms control framework is established; and\n**(8)**\ncalls on the administration to continue to engage the People\u2019s Republic of China in further bilateral talks on nuclear risk reduction and arms control, and to pursue new multilateral arms control efforts.",
      "versionDate": "2025-02-05",
      "versionType": "IS"
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
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "100",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the continued value of arms control agreements and negotiated constraints on Russian and Chinese strategic nuclear forces.",
      "type": "HRES"
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
        "name": "International Affairs",
        "updateDate": "2025-02-20T14:50:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119sres61",
          "measure-number": "61",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres61v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution condemns Russia's nuclear escalatory rhetoric and implied threats on the potential use of nuclear weapons in the context of its invasion of Ukraine. The resolution also (1) condemns Russia's purported suspension of participation in the New START Treaty, (2) emphasizes the value of arms control agreements between the United States and Russia, and (3) calls on the administration to continue pursuing nuclear arms control and risk reduction with Russia and China.</p>"
        },
        "title": "A resolution expressing support for the continued value of arms control agreements and negotiated constraints on Russian and Chinese strategic nuclear forces."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres61.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution condemns Russia's nuclear escalatory rhetoric and implied threats on the potential use of nuclear weapons in the context of its invasion of Ukraine. The resolution also (1) condemns Russia's purported suspension of participation in the New START Treaty, (2) emphasizes the value of arms control agreements between the United States and Russia, and (3) calls on the administration to continue pursuing nuclear arms control and risk reduction with Russia and China.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119sres61"
    },
    "title": "A resolution expressing support for the continued value of arms control agreements and negotiated constraints on Russian and Chinese strategic nuclear forces."
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution condemns Russia's nuclear escalatory rhetoric and implied threats on the potential use of nuclear weapons in the context of its invasion of Ukraine. The resolution also (1) condemns Russia's purported suspension of participation in the New START Treaty, (2) emphasizes the value of arms control agreements between the United States and Russia, and (3) calls on the administration to continue pursuing nuclear arms control and risk reduction with Russia and China.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119sres61"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres61is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing support for the continued value of arms control agreements and negotiated constraints on Russian and Chinese strategic nuclear forces.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:23Z"
    },
    {
      "title": "A resolution expressing support for the continued value of arms control agreements and negotiated constraints on Russian and Chinese strategic nuclear forces.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T11:56:38Z"
    }
  ]
}
```
