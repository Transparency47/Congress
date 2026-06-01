# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/344?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/344
- Title: Anti-Congestion Tax Act
- Congress: 119
- Bill type: HR
- Bill number: 344
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-03-12T08:06:39Z
- Update date including text: 2025-03-12T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-13 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-13 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/344",
    "number": "344",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Anti-Congestion Tax Act",
    "type": "HR",
    "updateDate": "2025-03-12T08:06:39Z",
    "updateDateIncludingText": "2025-03-12T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-14T15:33:49Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-13T17:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NJ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr344ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 344\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Gottheimer (for himself and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo condition the receipt of certain grants by the Metropolitan Transportation Authority on exempting certain drivers from congestion fees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Anti-Congestion Tax Act .\n#### 2. Condition on receipt of capital investment grants\n##### (a) In general\nNotwithstanding any other provision of law, the Secretary of Transportation may not award a capital investment grant described in section 5338(d) of title 49, United States Code, to the Metropolitan Transportation Authority for a project in New York State until the Secretary certifies that any vehicle entering the congestion tolling zone using a vehicular crossing known as the Holland Tunnel, the Lincoln Tunnel, or the George Washington Bridge, or any other vehicular crossing for the use of crossing immediately before entry into the congestion tolling zone, receives an exemption as follows: The vehicle is credited an amount equal to the toll charged to such vehicle for the use of such crossing immediately before entry into the congestion tolling zone from the amount of the congestion toll charged to such vehicle for purposes of entering the congestion tolling zone.\n##### (b) Rule of construction for George Washington Bridge\nFor purposes of subsection (a), a vehicle receives an exemption while crossing the George Washington Bridge if such vehicle is treated in the same manner as a vehicle crossing the Henry Hudson Bridge is treated on the first date on which the congestion toll is charged.\n##### (c) Effective date\nSubsection (a) shall apply with respect to a grant awarded on or after the first date on which the congestion toll is charged.\n##### (d) Definitions\nIn this section, the following definitions apply:\n**(1) Congestion toll**\nThe term congestion toll means a toll charged for entry into or remaining in the congestion tolling zone.\n**(2) Congestion tolling zone**\nThe term congestion tolling zone means any roadways, bridges, tunnels, approaches, or ramps that are located within, or enter to, the geographic area in the borough of Manhattan south of and inclusive of Sixtieth Street to the extent practicable, but does not include the Franklin D. Roosevelt Drive.\n#### 3. Credit for certain congestion tolls\n##### (a) In general\nSubpart B of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding after section 30D the following new section:\n30E. Certain congestion tolls (a) In general There shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the sum of any congestion toll (as such term is defined in section 2(d) of the Anti-Congestion Tax Act ) paid or incurred during the taxable year by such taxpayer for the use of any qualified vehicular crossing immediately before entry into the congestion tolling zone (as such term is defined in section 2(d) of the Anti-Congestion Tax Act ). (b) Qualified vehicular crossing For purposes of this section, the term qualified vehicular crossing means any of the vehicular crossing known as the Holland Tunnel, the Lincoln Tunnel, the George Washington Bridge, or any other vehicular crossing for the use of crossing immediately before entry into the congestion tolling zone. (c) No double benefit The amount of any deduction or other credit allowable under this chapter for a congestion toll for which a credit is allowable under subsection (a) shall be reduced by the amount of credit allowed under such subsection. .\n##### (b) Clerical amendment\nThe table of sections for such subpart B is amended by inserting after the item relating to section 30D the following new item:\nSec. 30E. Certain congestion tolls. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of enactment of this Act.",
      "versionDate": "2025-01-13",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-14T18:10:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr344",
          "measure-number": "344",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr344v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Anti-Congestion Tax Act </strong></p><p>This bill prohibits the Department of Transportation (DOT) from awarding capital investment grants to the Metropolitan Transportation Authority (MTA) for projects in New York until DOT certifies that vehicles using certain crossings to enter into Manhattan's congestion tolling zone\u00a0receive exemptions from congestion tolls.\u00a0The vehicular crossings include the Holland Tunnel, the Lincoln Tunnel, the George Washington Bridge,\u00a0and any other crossing immediately before entry into the congestion tolling zone.</p><p>As background, the\u00a0MTA's Central Business District Tolling Program for New York City charges drivers a toll to enter an area in Manhattan designated as the Congestion Relief Zone.\u00a0Under the bill, <em>c</em><em>ongestion tolling zone</em> generally means any roadways, bridges, tunnels, approaches, or ramps that are located within, or enter to, the Congestion Relief Zone, with some modifications.</p><p>Specifically, the bill requires the MTA to credit a vehicle for the vehicular crossing toll from the amount of the congestion toll charged to the vehicle for entering the congestion tolling zone.</p><p>Further,\u00a0the bill allows drivers entering Manhattan using any of the vehicular\u00a0crossings immediately before entry into the congestion tolling zone\u00a0to receive a federal tax credit at the end of the year equal to the amount paid in congestion tolls for using the crossing.\u00a0</p><p><br/><br/><br/><br/></p>"
        },
        "title": "Anti-Congestion Tax Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr344.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Anti-Congestion Tax Act </strong></p><p>This bill prohibits the Department of Transportation (DOT) from awarding capital investment grants to the Metropolitan Transportation Authority (MTA) for projects in New York until DOT certifies that vehicles using certain crossings to enter into Manhattan's congestion tolling zone\u00a0receive exemptions from congestion tolls.\u00a0The vehicular crossings include the Holland Tunnel, the Lincoln Tunnel, the George Washington Bridge,\u00a0and any other crossing immediately before entry into the congestion tolling zone.</p><p>As background, the\u00a0MTA's Central Business District Tolling Program for New York City charges drivers a toll to enter an area in Manhattan designated as the Congestion Relief Zone.\u00a0Under the bill, <em>c</em><em>ongestion tolling zone</em> generally means any roadways, bridges, tunnels, approaches, or ramps that are located within, or enter to, the Congestion Relief Zone, with some modifications.</p><p>Specifically, the bill requires the MTA to credit a vehicle for the vehicular crossing toll from the amount of the congestion toll charged to the vehicle for entering the congestion tolling zone.</p><p>Further,\u00a0the bill allows drivers entering Manhattan using any of the vehicular\u00a0crossings immediately before entry into the congestion tolling zone\u00a0to receive a federal tax credit at the end of the year equal to the amount paid in congestion tolls for using the crossing.\u00a0</p><p><br/><br/><br/><br/></p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr344"
    },
    "title": "Anti-Congestion Tax Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Anti-Congestion Tax Act </strong></p><p>This bill prohibits the Department of Transportation (DOT) from awarding capital investment grants to the Metropolitan Transportation Authority (MTA) for projects in New York until DOT certifies that vehicles using certain crossings to enter into Manhattan's congestion tolling zone\u00a0receive exemptions from congestion tolls.\u00a0The vehicular crossings include the Holland Tunnel, the Lincoln Tunnel, the George Washington Bridge,\u00a0and any other crossing immediately before entry into the congestion tolling zone.</p><p>As background, the\u00a0MTA's Central Business District Tolling Program for New York City charges drivers a toll to enter an area in Manhattan designated as the Congestion Relief Zone.\u00a0Under the bill, <em>c</em><em>ongestion tolling zone</em> generally means any roadways, bridges, tunnels, approaches, or ramps that are located within, or enter to, the Congestion Relief Zone, with some modifications.</p><p>Specifically, the bill requires the MTA to credit a vehicle for the vehicular crossing toll from the amount of the congestion toll charged to the vehicle for entering the congestion tolling zone.</p><p>Further,\u00a0the bill allows drivers entering Manhattan using any of the vehicular\u00a0crossings immediately before entry into the congestion tolling zone\u00a0to receive a federal tax credit at the end of the year equal to the amount paid in congestion tolls for using the crossing.\u00a0</p><p><br/><br/><br/><br/></p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr344"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr344ih.xml"
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
      "title": "Anti-Congestion Tax Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Anti-Congestion Tax Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To condition the receipt of certain grants by the Metropolitan Transportation Authority on exempting certain drivers from congestion fees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:18Z"
    }
  ]
}
```
