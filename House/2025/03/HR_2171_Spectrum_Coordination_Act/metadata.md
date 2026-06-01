# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2171?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2171
- Title: Spectrum Coordination Act
- Congress: 119
- Bill type: HR
- Bill number: 2171
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-06-02T14:57:56Z
- Update date including text: 2025-06-02T14:57:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2171",
    "number": "2171",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001306",
        "district": "12",
        "firstName": "Troy",
        "fullName": "Rep. Balderson, Troy [R-OH-12]",
        "lastName": "Balderson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Spectrum Coordination Act",
    "type": "HR",
    "updateDate": "2025-06-02T14:57:56Z",
    "updateDateIncludingText": "2025-06-02T14:57:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:02:20Z",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2171ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2171\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Balderson (for himself and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo improve Federal coordination with respect to spectrum management, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Spectrum Coordination Act .\n#### 2. Improving spectrum management\nPart A of the National Telecommunications and Information Administration Organization Act is amended by adding at the end the following:\n106. Improving spectrum management (a) Federal coordination procedures (1) Notice With respect to each spectrum action, the Assistant Secretary shall file in the public record with respect to such spectrum action, not later than the end of the period for submitting comments to the Commission with respect to such spectrum action, information (redacted as necessary if the information is protected from disclosure for a reason described in paragraph (3)) regarding\u2014 (A) the date on which the Commission provided to the Assistant Secretary notice of the spectrum action, as required under the Memorandum; (B) the Federal entities that may be impacted by the spectrum action; (C) the date on which the Assistant Secretary provided to the Federal entities described in subparagraph (B) notice of the spectrum action; (D) a summary of technical or procedural concerns, if any, of Federal entities with respect to the spectrum action; and (E) a summary of policy concerns, if any, of the Assistant Secretary with respect to the spectrum action. (2) Final rule If the Commission promulgates a final rule under section 553 of title 5, United States Code, involving a spectrum action, the Commission shall prepare, make available to the public, and publish in the Federal Register along with the final rule an interagency coordination summary that describes\u2014 (A) the date on which the Commission provided to the Assistant Secretary notice of the spectrum action, as required under the Memorandum; (B) whether concerns were raised under subparagraph (D) or subparagraph (E) of paragraph (1) and, if so, the concerns raised; and (C) how any such concerns were resolved. (3) Rule of construction Nothing in this subsection may be construed to require the disclosure of classified information, or other information reflecting technical, procedural, or policy concerns that are exempt from disclosure under section 552 of title 5, United States Code. (b) Memorandum (1) Memorandum updates Not later than 3 years after the date of the enactment of this section, and not less frequently than every 4 years thereafter, the Commission and the NTIA shall update the Memorandum. (2) Nature of updates In updating the Memorandum under paragraph (1), the Commission and the NTIA shall ensure that each update reflects changing technological, procedural, and policy circumstances, as determined necessary and appropriate by the Commission and the NTIA. (c) Definitions In this section: (1) Memorandum The term Memorandum means the Memorandum of Understanding between the Commission and the NTIA (relating to increased coordination between Federal spectrum management agencies to promote the efficient use of the radio spectrum in the public interest), signed on August 1, 2022, or any successor memorandum. (2) Spectrum action The term spectrum action means any proposed action by the Commission to reallocate radio frequency spectrum that is anticipated to result in a system of competitive bidding conducted under section 309(j) of the Communications Act of 1934 ( 47 U.S.C. 309(j) ) or licensing that could potentially impact the spectrum operations of a Federal entity. .",
      "versionDate": "2025-03-18",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-31T16:23:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-18",
    "originChamber": "House",
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
          "measure-id": "id119hr2171",
          "measure-number": "2171",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-18",
          "originChamber": "HOUSE",
          "update-date": "2025-06-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2171v00",
            "update-date": "2025-06-02"
          },
          "action-date": "2025-03-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Spectrum Coordination Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) and the National Telecommunications and Information Administration (NTIA) to document publicly their interagency coordination efforts with respect to certain spectrum reallocation actions potentially affecting federal spectrum users.\u00a0</p><p>Specifically, for any proposal by the FCC to reallocate radio frequency spectrum in a manner anticipated to result in an auction or licensing that may impact federal spectrum use, the NTIA must file certain information in the public docket for the action during the public comment period. Specifically, this filing must include (1) the date on which the FCC notified the NTIA of the proposed action; (2) any federal entities that may be affected by the proposal; (3) the date on which the NTIA notified those entities of the proposal; and (4) a summary of any technical, procedural, or policy concerns of potentially affected federal entities or the NTIA.\u00a0</p><p>In the event that the FCC promulgates a final rule involving such a spectrum action, the FCC must publish in the Federal Register along with the final rule an interagency coordination summary describing (1) the date on which the FCC notified the NTIA of the action; and (2) whether the NTIA or any potentially affected federal entity raised concerns regarding the action and, if so, how they were addressed.\u00a0</p><p>Separately, the FCC and the NTIA must update the Memorandum of Understanding between them within three years of the bill\u2019s enactment and periodically thereafter. Updates must reflect changing technological, procedural, and policy circumstances.</p>"
        },
        "title": "Spectrum Coordination Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2171.xml",
    "summary": {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Spectrum Coordination Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) and the National Telecommunications and Information Administration (NTIA) to document publicly their interagency coordination efforts with respect to certain spectrum reallocation actions potentially affecting federal spectrum users.\u00a0</p><p>Specifically, for any proposal by the FCC to reallocate radio frequency spectrum in a manner anticipated to result in an auction or licensing that may impact federal spectrum use, the NTIA must file certain information in the public docket for the action during the public comment period. Specifically, this filing must include (1) the date on which the FCC notified the NTIA of the proposed action; (2) any federal entities that may be affected by the proposal; (3) the date on which the NTIA notified those entities of the proposal; and (4) a summary of any technical, procedural, or policy concerns of potentially affected federal entities or the NTIA.\u00a0</p><p>In the event that the FCC promulgates a final rule involving such a spectrum action, the FCC must publish in the Federal Register along with the final rule an interagency coordination summary describing (1) the date on which the FCC notified the NTIA of the action; and (2) whether the NTIA or any potentially affected federal entity raised concerns regarding the action and, if so, how they were addressed.\u00a0</p><p>Separately, the FCC and the NTIA must update the Memorandum of Understanding between them within three years of the bill\u2019s enactment and periodically thereafter. Updates must reflect changing technological, procedural, and policy circumstances.</p>",
      "updateDate": "2025-06-02",
      "versionCode": "id119hr2171"
    },
    "title": "Spectrum Coordination Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Spectrum Coordination Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) and the National Telecommunications and Information Administration (NTIA) to document publicly their interagency coordination efforts with respect to certain spectrum reallocation actions potentially affecting federal spectrum users.\u00a0</p><p>Specifically, for any proposal by the FCC to reallocate radio frequency spectrum in a manner anticipated to result in an auction or licensing that may impact federal spectrum use, the NTIA must file certain information in the public docket for the action during the public comment period. Specifically, this filing must include (1) the date on which the FCC notified the NTIA of the proposed action; (2) any federal entities that may be affected by the proposal; (3) the date on which the NTIA notified those entities of the proposal; and (4) a summary of any technical, procedural, or policy concerns of potentially affected federal entities or the NTIA.\u00a0</p><p>In the event that the FCC promulgates a final rule involving such a spectrum action, the FCC must publish in the Federal Register along with the final rule an interagency coordination summary describing (1) the date on which the FCC notified the NTIA of the action; and (2) whether the NTIA or any potentially affected federal entity raised concerns regarding the action and, if so, how they were addressed.\u00a0</p><p>Separately, the FCC and the NTIA must update the Memorandum of Understanding between them within three years of the bill\u2019s enactment and periodically thereafter. Updates must reflect changing technological, procedural, and policy circumstances.</p>",
      "updateDate": "2025-06-02",
      "versionCode": "id119hr2171"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2171ih.xml"
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
      "title": "Spectrum Coordination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Spectrum Coordination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve Federal coordination with respect to spectrum management, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:48:28Z"
    }
  ]
}
```
