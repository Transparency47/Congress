# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/5?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sconres/5
- Title: A concurrent resolution expressing the sense of Congress that the proposed "joint interpretation" of Annex 14-C of the United States-Mexico-Canada Agreement prepared by United States Trade Representative Katherine Tai is of no legal effect with respect to the United States or any United States person unless it is approved by Congress.
- Congress: 119
- Bill type: SCONRES
- Bill number: 5
- Origin chamber: Senate
- Introduced date: 2025-01-15
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in Senate
- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Referred to the Committee on Finance. (text: CR S187)
- Latest action: 2025-01-15: Introduced in Senate

## Actions

- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Referred to the Committee on Finance. (text: CR S187)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sconres/5",
    "number": "5",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001319",
        "district": "",
        "firstName": "Katie",
        "fullName": "Sen. Britt, Katie Boyd [R-AL]",
        "lastName": "Britt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "A concurrent resolution expressing the sense of Congress that the proposed \"joint interpretation\" of Annex 14-C of the United States-Mexico-Canada Agreement prepared by United States Trade Representative Katherine Tai is of no legal effect with respect to the United States or any United States person unless it is approved by Congress.",
    "type": "SCONRES",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Finance. (text: CR S187)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T22:15:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres5is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. CON. RES. 5\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2025 Mrs. Britt (for herself and Mr. Tuberville ) submitted the following concurrent resolution; which was referred to the Committee on Finance\nCONCURRENT RESOLUTION\nExpressing the sense of Congress that the proposed joint interpretation of Annex 14-C of the United States-Mexico-Canada Agreement prepared by United States Trade Representative Katherine Tai is of no legal effect with respect to the United States or any United States person unless it is approved by Congress.\nThat it is the sense of Congress that\u2014\n**(1)**\nthe proposed joint interpretation of Annex 14-C of the USMCA (as defined in section 3 of the United States-Mexico-Canada Agreement Implementation Act ( 19 U.S.C. 4502 )) prepared by Ambassador Katherine Tai is of no legal effect with respect to the United States or any United States person, unless it is approved by Congress; and\n**(2)**\nthe Office of the United States Trade Representative, the Department of State, or any other agency of the United States cannot invoke the joint interpretation in any legal proceeding or assert that it has any legal consequence for any claims made by a United States person, unless and until the joint interpretation is formally approved by Congress.",
      "versionDate": "2025-01-15",
      "versionType": "IS"
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
        "updateDate": "2025-01-27T22:39:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119sconres5",
          "measure-number": "5",
          "measure-type": "sconres",
          "orig-publish-date": "2025-01-15",
          "originChamber": "SENATE",
          "update-date": "2025-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sconres5v00",
            "update-date": "2025-02-18"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This concurrent resolution states that, unless it is approved by Congress, the proposed joint interpretation of Annex 14-C of the United States-Mexico-Canada Agreement (USMCA) prepared by Ambassador Katherine Tai (1) is of no legal effect with respect to the United States or any U.S. person, and (2) cannot be invoked by any federal agency in any legal proceeding nor may a federal agency assert that it has any legal consequences for claims made by a U.S. person.\u00a0(Annex 14-C of the USMCA concerns certain investment claims under the North American Free Trade Agreement, the agreement which preceded USMCA.)</p>"
        },
        "title": "A concurrent resolution expressing the sense of Congress that the proposed \"joint interpretation\" of Annex 14-C of the United States-Mexico-Canada Agreement prepared by United States Trade Representative Katherine Tai is of no legal effect with respect to the United States or any United States person unless it is approved by Congress."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sconres/BILLSUM-119sconres5.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This concurrent resolution states that, unless it is approved by Congress, the proposed joint interpretation of Annex 14-C of the United States-Mexico-Canada Agreement (USMCA) prepared by Ambassador Katherine Tai (1) is of no legal effect with respect to the United States or any U.S. person, and (2) cannot be invoked by any federal agency in any legal proceeding nor may a federal agency assert that it has any legal consequences for claims made by a U.S. person.\u00a0(Annex 14-C of the USMCA concerns certain investment claims under the North American Free Trade Agreement, the agreement which preceded USMCA.)</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119sconres5"
    },
    "title": "A concurrent resolution expressing the sense of Congress that the proposed \"joint interpretation\" of Annex 14-C of the United States-Mexico-Canada Agreement prepared by United States Trade Representative Katherine Tai is of no legal effect with respect to the United States or any United States person unless it is approved by Congress."
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This concurrent resolution states that, unless it is approved by Congress, the proposed joint interpretation of Annex 14-C of the United States-Mexico-Canada Agreement (USMCA) prepared by Ambassador Katherine Tai (1) is of no legal effect with respect to the United States or any U.S. person, and (2) cannot be invoked by any federal agency in any legal proceeding nor may a federal agency assert that it has any legal consequences for claims made by a U.S. person.\u00a0(Annex 14-C of the USMCA concerns certain investment claims under the North American Free Trade Agreement, the agreement which preceded USMCA.)</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119sconres5"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres5is.xml"
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
      "title": "A concurrent resolution expressing the sense of Congress that the proposed \"joint interpretation\" of Annex 14-C of the United States-Mexico-Canada Agreement prepared by United States Trade Representative Katherine Tai is of no legal effect with respect to the United States or any United States person unless it is approved by Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-17T05:18:21Z"
    },
    {
      "title": "A concurrent resolution expressing the sense of Congress that the proposed \"joint interpretation\" of Annex 14-C of the United States-Mexico-Canada Agreement prepared by United States Trade Representative Katherine Tai is of no legal effect with respect to the United States or any United States person unless it is approved by Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-16T11:56:18Z"
    }
  ]
}
```
