# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/460?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/460
- Title: Supporting Made in America Energy Act
- Congress: 119
- Bill type: S
- Bill number: 460
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/460",
    "number": "460",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Supporting Made in America Energy Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T18:28:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "KS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ID"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "LA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MS"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AK"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WY"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ID"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "UT"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WY"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s460is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 460\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Daines (for himself, Mr. Marshall , Mr. Risch , Mr. Cassidy , Mrs. Hyde-Smith , Ms. Murkowski , Mr. Sheehy , Ms. Lummis , Mr. Crapo , Mr. Curtis , Mr. Barrasso , and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo promote domestic energy production, to require onshore and offshore oil and natural gas lease sales, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Made in America Energy Act .\n#### 2. Required onshore and offshore oil and natural gas leasing\n##### (a) Onshore lease sales\n**(1) Annual lease sales**\nNotwithstanding any other provision of law, in accordance with the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ), beginning in fiscal year 2025, the Secretary of the Interior (referred to in this section as the Secretary ) shall conduct a minimum of 4 oil and natural gas lease sales annually in each of the following States:\n**(A)**\nWyoming.\n**(B)**\nNew Mexico.\n**(C)**\nColorado.\n**(D)**\nUtah.\n**(E)**\nMontana.\n**(F)**\nNorth Dakota.\n**(G)**\nOklahoma.\n**(H)**\nNevada.\n**(I)**\nAny other State in which there is land available for oil and natural gas leasing under that Act.\n**(2) Requirement**\nIn conducting a lease sale under paragraph (1) in a State described in that paragraph, the Secretary shall offer all parcels eligible for oil and gas development under the resource management plan in effect for the State.\n**(3) Replacement sales**\nIf, for any reason, a lease sale under paragraph (1) for a calendar year is canceled, delayed, or deferred, including for a lack of eligible parcels, the Secretary shall conduct a replacement sale during the same calendar year.\n##### (b) Offshore lease sales\n**(1) Gulf of mexico region annual lease sales**\n**(A) In general**\nNotwithstanding any other provision of law, beginning in fiscal year 2026, the Secretary shall conduct a minimum of 2 region-wide oil and natural gas lease sales annually in the Gulf of Mexico Region of the outer Continental Shelf, which shall\u2014\n**(i)**\noffer the same lease form, lease terms, economic conditions, and stipulations as contained in the final notice of sale entitled Gulf of Mexico Outer Continental Shelf Oil and Gas Lease Sale 261 (88 Fed. Reg. 80750 (November 20, 2023)); and\n**(ii)**\ninclude\u2014\n**(I)**\nthe Central Gulf of Mexico Planning Area, as described in the 2017\u20132022 Outer Continental Shelf Oil and Gas Leasing Proposed Final Program (November 2016); and\n**(II)**\nthe Western Gulf of Mexico Planning Area, as described in the 2017\u20132022 Outer Continental Shelf Oil and Gas Leasing Proposed Final Program (November 2016).\n**(B) Timing**\nIn conducting the offshore lease sales under subparagraph (A), the Secretary shall conduct a lease sale under that subparagraph not later than each of the following dates:\n**(i)**\nMarch 31, 2026.\n**(ii)**\nAugust 31, 2026.\n**(iii)**\nMarch 31, 2027.\n**(iv)**\nAugust 31, 2027.\n**(v)**\nMarch 31, 2028.\n**(vi)**\nAugust 31, 2028.\n**(vii)**\nMarch 31, 2029.\n**(viii)**\nAugust 31, 2029.\n**(ix)**\nMarch 31, 2030.\n**(x)**\nAugust 31, 2030.\n**(xi)**\nMarch 31, 2031.\n**(xii)**\nAugust 31, 2031.\n**(xiii)**\nMarch 31, 2032.\n**(xiv)**\nAugust 31, 2032.\n**(xv)**\nMarch 31, 2033.\n**(xvi)**\nAugust 31, 2033.\n**(xvii)**\nMarch 31, 2034.\n**(xviii)**\nAugust 31, 2034.\n**(xix)**\nMarch 31, 2035.\n**(xx)**\nAugust 31, 2035.\n**(2) Moratorium on oil and gas leasing in the Eastern Gulf of Mexico**\nSection 104 of the Gulf of Mexico Energy Security Act of 2006 ( 43 U.S.C. 1331 note; Public Law 109\u2013432 ) is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin the matter preceding paragraph (1), by striking June 30, 2022 and inserting December 31, 2035 ;\n**(ii)**\nin paragraph (2), by striking or after the semicolon;\n**(iii)**\nin paragraph (3)(B)(iii), by striking the period at the end and inserting a semicolon; and\n**(iv)**\nby adding at the end the following:\n(4) any area in the South Atlantic Planning Area (as designated by the Bureau of Ocean Energy Management as of the date of enactment of this paragraph); or (5) any area in the Straits of Florida Planning Area (as designated by the Bureau of Ocean Energy Management as of the date of enactment of this paragraph). ; and\n**(B)**\nby adding at the end the following:\n(d) Effect on certain leases The moratoria under subsection (a) shall not affect valid existing leases in effect on the date of enactment of this subsection. (e) Environmental exceptions Notwithstanding subsection (a), the Secretary may issue leases in areas described in that subsection for environmental conservation purposes, including the purposes of shore protection, beach nourishment and restoration, wetlands restoration, and habitat protection. .\n**(3) Lease sales in Alaska region**\n**(A) In general**\nThe Secretary of the Interior shall conduct a minimum of 6 offshore lease sales during the 10-year period beginning on the date of enactment of this Act in the Cook Inlet Planning Area as identified in the 2017\u20132022 Outer Continental Shelf Oil and Gas Leasing Proposed Final Program published on November 18, 2016, by the Bureau of Ocean Energy Management (as announced in the notice of availability of the Bureau of Ocean Energy Management entitled Notice of Availability of the 2017\u20132022 Outer Continental Shelf Oil and Gas Leasing Proposed Final Program (81 Fed. Reg. 84612 (November 23, 2016))).\n**(B) Requirements**\n**(i) Area offered for lease**\nThe Secretary of the Interior shall offer not fewer than 1,000,000 acres for each offshore lease sale conducted under subparagraph (A).\n**(ii) Issuance of leases**\nIf any acceptable bids have been received for any tract offered in a lease sale conducted under subparagraph (A), the Secretary of the Interior shall issue the lease not later than 90 days after the lease sale to the highest bid on the tract offered.\n**(iii) Royalty rate**\nThe royalty rate for each lease issued pursuant to a lease sale conducted under subparagraph (A) shall be 12.5 percent.\n**(4) Outer Continental Shelf oil and gas leasing program**\nSection 18 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1344 ) is amended\u2014\n**(A)**\nin subsection (a), in the first sentence of the matter preceding paragraph (1), by striking subsections (c) and (d) of this section and inserting subsections (c) through (f) ;\n**(B)**\nby redesignating subsections (f) through (i) as subsections (g) through (j), respectively;\n**(C)**\nby inserting after subsection (e) the following:\n(f) Subsequent leasing programs (1) In general Not later than 36 months after conducting the first lease sale under an oil and gas leasing program prepared pursuant to this section, the Secretary shall begin preparing the subsequent oil and gas leasing program under this section. (2) Requirement Each subsequent oil and gas leasing program under this section shall be approved not later than 180 days before the expiration of the previous oil and gas leasing program. ; and\n**(D)**\nby indenting subsection (j) (as so redesignated) appropriately.\n##### (c) Prohibition\n**(1) In general**\nThe President shall not, through Executive order or any other administrative procedure, unreasonably pause, cancel, delay, defer, or otherwise impede or circumvent the Federal energy mineral leasing processes under the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ), the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 et seq. ), the Naval Petroleum Reserves Production Act of 1976 ( 42 U.S.C. 6501 et seq. ), or Public Law 115\u201397 (commonly known as the Tax Cuts and Jobs Act of 2017 ), or a related rulemaking process required by subchapter II of chapter 5, and chapter 7, of title 5, United States Code (commonly known as the Administrative Procedure Act ), without congressional approval.\n**(2) Rebuttable presumption**\nThere shall be a rebuttable presumption that any attempt by the President to pause, cancel, delay, defer, or otherwise impede or circumvent any Federal energy mineral leasing process under the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ), the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 et seq. ), the Naval Petroleum Reserves Production Act of 1976 ( 42 U.S.C. 6501 et seq. ), or Public Law 115\u201397 (commonly known as the Tax Cuts and Jobs Act of 2017 ), or a related rulemaking process required by subchapter II of chapter 5, and chapter 7, of title 5, United States Code (commonly known as the Administrative Procedure Act ), without congressional approval, is a violation of the applicable law.",
      "versionDate": "2025-02-06",
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
        "name": "Energy",
        "updateDate": "2025-03-12T14:18:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s460",
          "measure-number": "460",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s460v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Supporting Made in America Energy Act</strong></p><p>This bill requires oil and natural gas lease sales that include\u00a0certain public land and waters, prohibits lease sales in other areas, and establishes related requirements.</p><p>Beginning in FY2025, the Department of the Interior must conduct a minimum of four onshore lease sales annually in each state that has federal land available for oil and natural gas leasing. If a lease sale is canceled, delayed, or deferred, Interior must conduct a replacement sale during the same year.\u00a0</p><p>Beginning in FY2026, Interior must conduct a minimum of two offshore, region-wide lease sales annually in the Gulf of Mexico Region of the Outer Continental Shelf (OCS) by specified dates. The sales must include the Central Gulf of Mexico Planning Area and the Western Gulf of Mexico Planning Area.</p><p>Interior must also conduct a minimum of six offshore lease sales of at least 1 million acres each over a 10-year period in the Cook Inlet Planning Area. The bill sets a 12.5% royalty rate for such leases.</p><p>Interior must plan and approve the subsequent OCS oil and gas leasing programs by specified deadlines.</p><p>The bill extends through 2035 a moratorium on oil and gas leasing in certain eastern and central portions of the Gulf of Mexico and expands the moratorium to include the South Atlantic Planning Area and the Straits of Florida Planning Area.</p><p>The bill also requires the President to obtain congressional approval before impeding or circumventing certain federal energy mineral leasing processes.</p>"
        },
        "title": "Supporting Made in America Energy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s460.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Made in America Energy Act</strong></p><p>This bill requires oil and natural gas lease sales that include\u00a0certain public land and waters, prohibits lease sales in other areas, and establishes related requirements.</p><p>Beginning in FY2025, the Department of the Interior must conduct a minimum of four onshore lease sales annually in each state that has federal land available for oil and natural gas leasing. If a lease sale is canceled, delayed, or deferred, Interior must conduct a replacement sale during the same year.\u00a0</p><p>Beginning in FY2026, Interior must conduct a minimum of two offshore, region-wide lease sales annually in the Gulf of Mexico Region of the Outer Continental Shelf (OCS) by specified dates. The sales must include the Central Gulf of Mexico Planning Area and the Western Gulf of Mexico Planning Area.</p><p>Interior must also conduct a minimum of six offshore lease sales of at least 1 million acres each over a 10-year period in the Cook Inlet Planning Area. The bill sets a 12.5% royalty rate for such leases.</p><p>Interior must plan and approve the subsequent OCS oil and gas leasing programs by specified deadlines.</p><p>The bill extends through 2035 a moratorium on oil and gas leasing in certain eastern and central portions of the Gulf of Mexico and expands the moratorium to include the South Atlantic Planning Area and the Straits of Florida Planning Area.</p><p>The bill also requires the President to obtain congressional approval before impeding or circumventing certain federal energy mineral leasing processes.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119s460"
    },
    "title": "Supporting Made in America Energy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Made in America Energy Act</strong></p><p>This bill requires oil and natural gas lease sales that include\u00a0certain public land and waters, prohibits lease sales in other areas, and establishes related requirements.</p><p>Beginning in FY2025, the Department of the Interior must conduct a minimum of four onshore lease sales annually in each state that has federal land available for oil and natural gas leasing. If a lease sale is canceled, delayed, or deferred, Interior must conduct a replacement sale during the same year.\u00a0</p><p>Beginning in FY2026, Interior must conduct a minimum of two offshore, region-wide lease sales annually in the Gulf of Mexico Region of the Outer Continental Shelf (OCS) by specified dates. The sales must include the Central Gulf of Mexico Planning Area and the Western Gulf of Mexico Planning Area.</p><p>Interior must also conduct a minimum of six offshore lease sales of at least 1 million acres each over a 10-year period in the Cook Inlet Planning Area. The bill sets a 12.5% royalty rate for such leases.</p><p>Interior must plan and approve the subsequent OCS oil and gas leasing programs by specified deadlines.</p><p>The bill extends through 2035 a moratorium on oil and gas leasing in certain eastern and central portions of the Gulf of Mexico and expands the moratorium to include the South Atlantic Planning Area and the Straits of Florida Planning Area.</p><p>The bill also requires the President to obtain congressional approval before impeding or circumventing certain federal energy mineral leasing processes.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119s460"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s460is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote domestic energy production, to require onshore and offshore oil and natural gas lease sales, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:31Z"
    },
    {
      "title": "Supporting Made in America Energy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting Made in America Energy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    }
  ]
}
```
