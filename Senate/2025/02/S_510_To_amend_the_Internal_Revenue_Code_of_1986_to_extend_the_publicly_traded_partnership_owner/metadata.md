# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/510?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/510
- Title: Financing Our Energy Future Act
- Congress: 119
- Bill type: S
- Bill number: 510
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-05-21T15:31:58Z
- Update date including text: 2026-05-21T15:31:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/510",
    "number": "510",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Financing Our Energy Future Act",
    "type": "S",
    "updateDate": "2026-05-21T15:31:58Z",
    "updateDateIncludingText": "2026-05-21T15:31:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T16:36:55Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "DE"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "WY"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "ME"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-11",
      "state": "ME"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "VA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "KS"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "UT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "ND"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s510is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 510\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Moran (for himself, Mr. Coons , Mr. Barrasso , Ms. Collins , Mr. King , Mr. Warner , Mr. Marshall , Mr. Cornyn , Mr. Curtis , Mr. Cramer , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the publicly traded partnership ownership structure to energy power generation projects and transportation fuels, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Financing Our Energy Future Act .\n#### 2. Green energy publicly traded partnerships\n##### (a) In general\nSection 7704(d)(1)(E) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking income and gains derived from the exploration and inserting\nincome and gains derived from\u2014 (i) the exploration ,\n**(2)**\nby inserting or before industrial source , and\n**(3)**\nby striking , or the transportation or storage and all that follows and inserting the following:\n(ii) the generation of electric power or thermal energy exclusively using any qualified energy resource (as defined in section 45(c)(1)), (iii) the operation of energy property (as defined in section 48(a)(3), determined without regard to any date by which the construction of the facility is required to begin), (iv) in the case of a facility described in paragraph (3) or (7) of section 45(d) (determined without regard to any placed in service date or date by which construction of the facility is required to begin), the accepting or processing of open-loop biomass or municipal solid waste, (v) the storage of electric power or thermal energy exclusively using energy storage technology (as defined in section 48(c)(6)), (vi) the generation, storage, or distribution of electric power or thermal energy exclusively using energy property that is combined heat and power system property (as defined in section 48(c)(3), determined without regard to subparagraph (B)(iii) thereof and without regard to any date by which the construction of the facility is required to begin), (vii) the transportation or storage of\u2014 (I) any fuel described in subsection (b), (c), (d), (e), or (k) of section 6426, or (II) liquified hydrogen or compressed hydrogen, (viii) the conversion of renewable biomass (as defined in subparagraph (I) of section 211(o)(1) of the Clean Air Act (as in effect on the date of the enactment of this clause)) into renewable fuel (as defined in subparagraph (J) of such section as so in effect), or the storage or transportation of such fuel, (ix) the production, storage, or transportation of any fuel which\u2014 (I) uses as its primary feedstock carbon oxides captured from an anthropogenic source or the atmosphere, (II) does not use as its primary feedstock carbon oxide which is deliberately released from naturally occurring subsurface springs, and (III) is determined by the Secretary, after consultation with the Secretary of Energy and the Administrator of the Environmental Protection Agency, to achieve a reduction of not less than a 60 percent in lifecycle greenhouse gas emissions (as defined in section 211(o)(1)(H) of the Clean Air Act, as in effect on the date of the enactment of this clause) compared to baseline lifecycle greenhouse gas emissions (as defined in section 211(o)(1)(C) of such Act, as so in effect), (x) the generation of electric power from a qualifying gasification project (as defined in section 48B(c)(1) without regard to subparagraph (C)) that is described in section 48B(d)(1)(B), (xi) in the case of a qualified facility (as defined in section 45Q(d), without regard to any date by which construction of the facility is required to begin) not less than 50 percent of the total carbon oxide production of which is qualified carbon oxide (as defined in section 45Q(c))\u2014 (I) the generation, availability for such generation, or storage of electric power at such facility, or (II) the capture of carbon dioxide by such facility, (xii) the generation of electric power or energy from any advanced nuclear facility (as defined in section 45J(d)(2)), or (xiii) the production, storage, or transportation of any renewable chemical which\u2014 (I) is produced in the United States (or in a territory or possession of the United States) from renewable biomass, (II) is not less than 95 percent biobased content, (III) is not sold or used for the production of any food, feed, fuel, or pharmaceuticals, (IV) is approved to use the USDA Certified Biobased Product label under section 9002(b) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8102(b) ), and (V) is a chemical intermediate (as such term is defined in section 3201.109 of title 7, Code of Federal Regulations (or successor regulations)), .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-02-11",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2545",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Financing Our Energy Future Act",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2025-05-05T18:54:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119s510",
          "measure-number": "510",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2026-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s510v00",
            "update-date": "2026-05-21"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Financing Our Energy Future Act</strong></p><p>This bill allows a publicly traded partnership to derive income from certain clean energy-related activities and still be treated as a partnership\u00a0for federal income tax purposes. </p><p>As background, a publicly traded partnership is a partnership whose interests are traded on an established securities market (or readily\u00a0tradable on a secondary market). A publicly traded partnership generally is treated\u00a0as a corporation for federal income tax purposes\u00a0unless 90% or more of such partnership\u2019s gross income is qualifying income.</p><p>Under current law, qualifying income includes\u00a0</p><ul><li>interest and dividends;</li><li>real property rents;</li><li>gain from the sale (or disposition) of real property;</li><li>income from certain activities related to minerals and natural resources, source carbon dioxide, and the transportation or storage of certain fuels; and</li><li>gain from the sale (or disposition) of a capital asset or commodities.</li></ul><p>Under the bill, the qualifying income is expanded to include income derived from \u00a0</p><ul><li>electric power (or thermal energy) generated from renewable energy sources (e.g., wind and solar energy), qualified\u00a0gasification projects, or advanced nuclear facilities;</li><li>accepting or processing open-loop biomass or municipal solid waste (by certain facilities);</li><li>the storage of electric power or thermal energy using certain energy storage technology;</li><li>the generation, storage, or distribution of electric power (or thermal energy) using combined heat and power system property;</li><li>fuels that use certain carbon oxides as primary feedstock;</li><li>certain renewable chemicals;</li><li>transportation or storage of liquefied or compressed hydrogen;</li><li>the conversion of renewable biomass; and</li><li>certain carbon capture and sequestration\u00a0facilities.</li></ul>"
        },
        "title": "Financing Our Energy Future Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s510.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Financing Our Energy Future Act</strong></p><p>This bill allows a publicly traded partnership to derive income from certain clean energy-related activities and still be treated as a partnership\u00a0for federal income tax purposes. </p><p>As background, a publicly traded partnership is a partnership whose interests are traded on an established securities market (or readily\u00a0tradable on a secondary market). A publicly traded partnership generally is treated\u00a0as a corporation for federal income tax purposes\u00a0unless 90% or more of such partnership\u2019s gross income is qualifying income.</p><p>Under current law, qualifying income includes\u00a0</p><ul><li>interest and dividends;</li><li>real property rents;</li><li>gain from the sale (or disposition) of real property;</li><li>income from certain activities related to minerals and natural resources, source carbon dioxide, and the transportation or storage of certain fuels; and</li><li>gain from the sale (or disposition) of a capital asset or commodities.</li></ul><p>Under the bill, the qualifying income is expanded to include income derived from \u00a0</p><ul><li>electric power (or thermal energy) generated from renewable energy sources (e.g., wind and solar energy), qualified\u00a0gasification projects, or advanced nuclear facilities;</li><li>accepting or processing open-loop biomass or municipal solid waste (by certain facilities);</li><li>the storage of electric power or thermal energy using certain energy storage technology;</li><li>the generation, storage, or distribution of electric power (or thermal energy) using combined heat and power system property;</li><li>fuels that use certain carbon oxides as primary feedstock;</li><li>certain renewable chemicals;</li><li>transportation or storage of liquefied or compressed hydrogen;</li><li>the conversion of renewable biomass; and</li><li>certain carbon capture and sequestration\u00a0facilities.</li></ul>",
      "updateDate": "2026-05-21",
      "versionCode": "id119s510"
    },
    "title": "Financing Our Energy Future Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Financing Our Energy Future Act</strong></p><p>This bill allows a publicly traded partnership to derive income from certain clean energy-related activities and still be treated as a partnership\u00a0for federal income tax purposes. </p><p>As background, a publicly traded partnership is a partnership whose interests are traded on an established securities market (or readily\u00a0tradable on a secondary market). A publicly traded partnership generally is treated\u00a0as a corporation for federal income tax purposes\u00a0unless 90% or more of such partnership\u2019s gross income is qualifying income.</p><p>Under current law, qualifying income includes\u00a0</p><ul><li>interest and dividends;</li><li>real property rents;</li><li>gain from the sale (or disposition) of real property;</li><li>income from certain activities related to minerals and natural resources, source carbon dioxide, and the transportation or storage of certain fuels; and</li><li>gain from the sale (or disposition) of a capital asset or commodities.</li></ul><p>Under the bill, the qualifying income is expanded to include income derived from \u00a0</p><ul><li>electric power (or thermal energy) generated from renewable energy sources (e.g., wind and solar energy), qualified\u00a0gasification projects, or advanced nuclear facilities;</li><li>accepting or processing open-loop biomass or municipal solid waste (by certain facilities);</li><li>the storage of electric power or thermal energy using certain energy storage technology;</li><li>the generation, storage, or distribution of electric power (or thermal energy) using combined heat and power system property;</li><li>fuels that use certain carbon oxides as primary feedstock;</li><li>certain renewable chemicals;</li><li>transportation or storage of liquefied or compressed hydrogen;</li><li>the conversion of renewable biomass; and</li><li>certain carbon capture and sequestration\u00a0facilities.</li></ul>",
      "updateDate": "2026-05-21",
      "versionCode": "id119s510"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s510is.xml"
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
      "title": "Financing Our Energy Future Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Financing Our Energy Future Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the publicly traded partnership ownership structure to energy power generation projects and transportation fuels, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:49Z"
    }
  ]
}
```
