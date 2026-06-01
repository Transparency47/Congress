# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/449?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/449
- Title: A resolution designating the week beginning on October 12, 2025, as "National Wildlife Refuge Week".
- Congress: 119
- Bill type: SRES
- Bill number: 449
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2026-04-08T20:23:59Z
- Update date including text: 2026-04-08T20:23:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S7098-7099)
- 2025-10-15 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-15 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7141)
- 2025-10-15 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-10-15 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S7098-7099)
- 2025-10-15 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-15 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7141)
- 2025-10-15 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-10-15 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/449",
    "number": "449",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "A resolution designating the week beginning on October 12, 2025, as \"National Wildlife Refuge Week\".",
    "type": "SRES",
    "updateDate": "2026-04-08T20:23:59Z",
    "updateDateIncludingText": "2026-04-08T20:23:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-15",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7141)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-10-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S7098-7099)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-09",
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
        "item": [
          {
            "date": "2025-10-15T22:45:55Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-10-10T01:20:36Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "LA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MD"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "RI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NM"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MD"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "DE"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "OR"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "ME"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "CA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MN"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "RI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres449is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 449\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Coons (for himself, Mr. Kennedy , Mr. Van Hollen , Mr. Reed , Mr. Heinrich , Ms. Alsobrooks , Ms. Blunt Rochester , Mr. Welch , Mr. Merkley , Ms. Collins , Mr. Padilla , Ms. Klobuchar , Mr. Whitehouse , Mr. Blumenthal , and Mr. Booker ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating the week beginning on October 12, 2025, as National Wildlife Refuge Week .\nThat the Senate\u2014\n**(1)**\ndesignates the week beginning on October 12, 2025, as National Wildlife Refuge Week ;\n**(2)**\nencourages the observance of National Wildlife Refuge Week with appropriate events and activities;\n**(3)**\nrecognizes the importance of national wildlife refuges to wildlife conservation, the protection of imperiled species and ecosystems, and wildlife-dependent recreational uses;\n**(4)**\nacknowledges the importance of national wildlife refuges for their recreational opportunities and contribution to local economies across the United States;\n**(5)**\nidentifies the significance of national wildlife refuges in advancing the traditions of wildlife observation, photography, and interpretation, as well as environmental education;\n**(6)**\nfinds that national wildlife refuges play a vital role in securing the hunting and fishing heritage of the United States for future generations;\n**(7)**\nrecognizes the important work of urban national wildlife refuges in welcoming racially and ethnically diverse urban communities that were long excluded, including work\u2014\n**(A)**\nto foster strong new conservation coalitions;\n**(B)**\nto provide education and employment opportunities to youth;\n**(C)**\nto improve communities;\n**(D)**\nto build trust in government; and\n**(E)**\nto connect individuals with nature;\n**(8)**\nrecognizes the commitment of the National Wildlife Refuge System to engagement, relationships, knowledge-sharing, and co-stewardship of National Wildlife Refuge System lands and waters with Tribes, Alaska Native Corporations, Alaska Native organizations, and the Native Hawaiian community;\n**(9)**\nacknowledges the role of national wildlife refuges in conserving waterfowl and waterfowl habitat under the Migratory Bird Treaty Act ( 16 U.S.C. 703 et seq. );\n**(10)**\nreaffirms the support of the Senate for wildlife conservation and the National Wildlife Refuge System; and\n**(11)**\nexpresses the intent of the Senate\u2014\n**(A)**\nto continue working to conserve wildlife; and\n**(B)**\nto support the management by the United States Fish and Wildlife Service of the National Wildlife Refuge System for current and future generations.",
      "versionDate": "2025-10-09",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres449ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 449\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Coons (for himself, Mr. Kennedy , Mr. Van Hollen , Mr. Reed , Mr. Heinrich , Ms. Alsobrooks , Ms. Blunt Rochester , Mr. Welch , Mr. Merkley , Ms. Collins , Mr. Padilla , Ms. Klobuchar , Mr. Whitehouse , Mr. Blumenthal , and Mr. Booker ) submitted the following resolution; which was referred to the Committee on the Judiciary\nOctober 15, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating the week beginning on October 12, 2025, as National Wildlife Refuge Week .\nThat the Senate\u2014\n**(1)**\ndesignates the week beginning on October 12, 2025, as National Wildlife Refuge Week ;\n**(2)**\nencourages the observance of National Wildlife Refuge Week with appropriate events and activities;\n**(3)**\nrecognizes the importance of national wildlife refuges to wildlife conservation, the protection of imperiled species and ecosystems, and wildlife-dependent recreational uses;\n**(4)**\nacknowledges the importance of national wildlife refuges for their recreational opportunities and contribution to local economies across the United States;\n**(5)**\nidentifies the significance of national wildlife refuges in advancing the traditions of wildlife observation, photography, and interpretation, as well as environmental education;\n**(6)**\nfinds that national wildlife refuges play a vital role in securing the hunting and fishing heritage of the United States for future generations;\n**(7)**\nrecognizes the important work of urban national wildlife refuges in welcoming racially and ethnically diverse urban communities that were long excluded, including work\u2014\n**(A)**\nto foster strong new conservation coalitions;\n**(B)**\nto provide education and employment opportunities to youth;\n**(C)**\nto improve communities;\n**(D)**\nto build trust in government; and\n**(E)**\nto connect individuals with nature;\n**(8)**\nrecognizes the commitment of the National Wildlife Refuge System to engagement, relationships, knowledge-sharing, and co-stewardship of National Wildlife Refuge System lands and waters with Tribes, Alaska Native Corporations, Alaska Native organizations, and the Native Hawaiian community;\n**(9)**\nacknowledges the role of national wildlife refuges in conserving waterfowl and waterfowl habitat under the Migratory Bird Treaty Act ( 16 U.S.C. 703 et seq. );\n**(10)**\nreaffirms the support of the Senate for wildlife conservation and the National Wildlife Refuge System; and\n**(11)**\nexpresses the intent of the Senate\u2014\n**(A)**\nto continue working to conserve wildlife; and\n**(B)**\nto support the management by the United States Fish and Wildlife Service of the National Wildlife Refuge System for current and future generations.",
      "versionDate": "2025-10-15",
      "versionType": "ATS"
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
        "actionDate": "2025-10-17",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "820",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting the designation of the week beginning on October 12, 2025, as \"National Wildlife Refuge Week\".",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Birds",
            "updateDate": "2025-12-08T16:21:08Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-12-08T16:21:08Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-12-08T16:21:08Z"
          },
          {
            "name": "Endangered and threatened species",
            "updateDate": "2025-12-08T16:21:08Z"
          },
          {
            "name": "Environmental education",
            "updateDate": "2025-12-08T16:21:08Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2025-12-08T16:21:08Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2025-12-08T16:21:08Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2025-12-08T16:21:08Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-08T16:21:08Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-12-08T16:21:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-05T16:21:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-09",
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
          "measure-id": "id119sres449",
          "measure-number": "449",
          "measure-type": "sres",
          "orig-publish-date": "2025-10-09",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres449v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-10-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution designates the week beginning on October 12, 2025, as National Wildlife Refuge Week.</p><p>The resolution acknowledges the importance of national wildlife refuges for their recreational opportunities and contribution to local economies.</p><p>Finally, the resolution reaffirms the support of the Senate for wildlife conservation and the National Wildlife Refuge System.</p>"
        },
        "title": "A resolution designating the week beginning on October 12, 2025, as \"National Wildlife Refuge Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres449.xml",
    "summary": {
      "actionDate": "2025-10-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates the week beginning on October 12, 2025, as National Wildlife Refuge Week.</p><p>The resolution acknowledges the importance of national wildlife refuges for their recreational opportunities and contribution to local economies.</p><p>Finally, the resolution reaffirms the support of the Senate for wildlife conservation and the National Wildlife Refuge System.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres449"
    },
    "title": "A resolution designating the week beginning on October 12, 2025, as \"National Wildlife Refuge Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates the week beginning on October 12, 2025, as National Wildlife Refuge Week.</p><p>The resolution acknowledges the importance of national wildlife refuges for their recreational opportunities and contribution to local economies.</p><p>Finally, the resolution reaffirms the support of the Senate for wildlife conservation and the National Wildlife Refuge System.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres449"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres449is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-10-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres449ats.xml"
        }
      ],
      "type": "ATS"
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
      "title": "A resolution designating the week beginning on October 12, 2025, as \"National Wildlife Refuge Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T02:33:13Z"
    },
    {
      "title": "A resolution designating the week beginning on October 12, 2025, as \"National Wildlife Refuge Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T10:56:18Z"
    }
  ]
}
```
