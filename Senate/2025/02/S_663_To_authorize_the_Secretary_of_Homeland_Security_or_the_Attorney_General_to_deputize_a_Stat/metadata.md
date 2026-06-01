# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/663?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/663
- Title: DEFENSE Act
- Congress: 119
- Bill type: S
- Bill number: 663
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2026-05-13T21:44:51Z
- Update date including text: 2026-05-13T21:44:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/663",
    "number": "663",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "DEFENSE Act",
    "type": "S",
    "updateDate": "2026-05-13T21:44:51Z",
    "updateDateIncludingText": "2026-05-13T21:44:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T18:20:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s663is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 663\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Cotton (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo authorize the Secretary of Homeland Security or the Attorney General to deputize a State or local law enforcement officer to protect certain events with temporary flight restrictions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disabling Enemy Flight Entry and Neutralizing Suspect Equipment Act or the DEFENSE Act .\n#### 2. Drone countermeasures to protect events\nSection 210G of the Homeland Security Act of 2002 ( 6 U.S.C. 124n ) is amended by adding at the end the following:\n(m) Stadium security (1) In general The Secretary or the Attorney General may deputize a State or local law enforcement officer to exercise the authority granted by subsection (a), except that the authority is granted solely for the purpose of protecting\u2014 (A) a site with respect to which a flight restriction is maintained pursuant to section 521 of division F of the Consolidated Appropriations Act, 2004 ( 49 U.S.C. 40103 note); (B) the location of an eligible large public gathering described in section 44812(c) of title 49, United States Code; or (C) a public gathering otherwise protected by a temporary flight restriction, at the discretion of the Administrator of the Federal Aviation Administration under the authority of section 40103(b) of title 49, United States Code. (2) Training required The Secretary or the Attorney General may deputize only a State or local law enforcement officer that has completed training in the use of the authority described in paragraph (1), as specified by the Secretary or Attorney General in coordination with the Secretary of Transportation and the Administrator of the Federal Aviation Administration. (3) Oversight The Secretary or the Attorney General, in coordination with the Secretary of Transportation and the Administrator of the Federal Aviation Administration, shall exercise oversight of the use of the authority described in paragraph (1) by a deputized State or local law enforcement officer. (4) Authorized equipment Equipment authorized for unmanned aircraft system detection, identification, monitoring, or tracking under this subsection shall be limited to systems or technologies that are included on a list of authorized equipment maintained by the Department, in coordination with the Department of Justice, the Federal Aviation Administration, the Federal Communications Commission, and the National Telecommunications and Information Administration. .",
      "versionDate": "2025-02-20",
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
        "actionDate": "2025-05-06",
        "text": "Referred to the Subcommittee on Aviation."
      },
      "number": "3207",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DEFENSE Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-13T17:39:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119s663",
          "measure-number": "663",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2026-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s663v00",
            "update-date": "2026-05-13"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Disabling Enemy Flight Entry and Neutralizing Suspect Equipment Act or the DEFENSE Act</strong></p><p>This bill allows the Department of Homeland Security (DHS) or the Department of Justice (DOJ) to deputize state or local law enforcement officers to take certain drone countermeasures\u00a0to\u00a0protect stadiums and other public gatherings.</p><p>Specifically, DHS or DOJ may provide state or local\u00a0law enforcement officers with the authority to identify, monitor, and track drones; warn drone operators; disrupt or take control of drones; or use reasonable force to disable, damage, and seize or destroy drones deemed to pose a threat.</p><p>This authority\u00a0applies for the purposes of protecting an event, stadium, or venue; certain large public gatherings (e.g., gatherings that are primarily outdoors with an estimated attendance of at least 100,000 people); or other public gatherings protected by specific temporary flight restrictions\u00a0imposed by the Federal Aviation Administration (FAA).</p><p>Prior to being deputized, a state or local law enforcement officer must complete training in the use of the drone countermeasure authority.</p><p>DHS or DOJ, in coordination with the Department of Transportation and the FAA, must exercise oversight over the\u00a0use of this\u00a0authority by deputized state or local law enforcement\u00a0officers.</p><p>Finally, the bill limits the equipment authorized for detecting, identifying, monitoring, or tracking drones to systems or technologies that are included on a list of authorized equipment maintained\u00a0by\u00a0DHS, in coordination with DOJ, the FAA, the Federal Communications Commission, and the National Telecommunications and Information Administration.</p>"
        },
        "title": "DEFENSE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s663.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disabling Enemy Flight Entry and Neutralizing Suspect Equipment Act or the DEFENSE Act</strong></p><p>This bill allows the Department of Homeland Security (DHS) or the Department of Justice (DOJ) to deputize state or local law enforcement officers to take certain drone countermeasures\u00a0to\u00a0protect stadiums and other public gatherings.</p><p>Specifically, DHS or DOJ may provide state or local\u00a0law enforcement officers with the authority to identify, monitor, and track drones; warn drone operators; disrupt or take control of drones; or use reasonable force to disable, damage, and seize or destroy drones deemed to pose a threat.</p><p>This authority\u00a0applies for the purposes of protecting an event, stadium, or venue; certain large public gatherings (e.g., gatherings that are primarily outdoors with an estimated attendance of at least 100,000 people); or other public gatherings protected by specific temporary flight restrictions\u00a0imposed by the Federal Aviation Administration (FAA).</p><p>Prior to being deputized, a state or local law enforcement officer must complete training in the use of the drone countermeasure authority.</p><p>DHS or DOJ, in coordination with the Department of Transportation and the FAA, must exercise oversight over the\u00a0use of this\u00a0authority by deputized state or local law enforcement\u00a0officers.</p><p>Finally, the bill limits the equipment authorized for detecting, identifying, monitoring, or tracking drones to systems or technologies that are included on a list of authorized equipment maintained\u00a0by\u00a0DHS, in coordination with DOJ, the FAA, the Federal Communications Commission, and the National Telecommunications and Information Administration.</p>",
      "updateDate": "2026-05-13",
      "versionCode": "id119s663"
    },
    "title": "DEFENSE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disabling Enemy Flight Entry and Neutralizing Suspect Equipment Act or the DEFENSE Act</strong></p><p>This bill allows the Department of Homeland Security (DHS) or the Department of Justice (DOJ) to deputize state or local law enforcement officers to take certain drone countermeasures\u00a0to\u00a0protect stadiums and other public gatherings.</p><p>Specifically, DHS or DOJ may provide state or local\u00a0law enforcement officers with the authority to identify, monitor, and track drones; warn drone operators; disrupt or take control of drones; or use reasonable force to disable, damage, and seize or destroy drones deemed to pose a threat.</p><p>This authority\u00a0applies for the purposes of protecting an event, stadium, or venue; certain large public gatherings (e.g., gatherings that are primarily outdoors with an estimated attendance of at least 100,000 people); or other public gatherings protected by specific temporary flight restrictions\u00a0imposed by the Federal Aviation Administration (FAA).</p><p>Prior to being deputized, a state or local law enforcement officer must complete training in the use of the drone countermeasure authority.</p><p>DHS or DOJ, in coordination with the Department of Transportation and the FAA, must exercise oversight over the\u00a0use of this\u00a0authority by deputized state or local law enforcement\u00a0officers.</p><p>Finally, the bill limits the equipment authorized for detecting, identifying, monitoring, or tracking drones to systems or technologies that are included on a list of authorized equipment maintained\u00a0by\u00a0DHS, in coordination with DOJ, the FAA, the Federal Communications Commission, and the National Telecommunications and Information Administration.</p>",
      "updateDate": "2026-05-13",
      "versionCode": "id119s663"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s663is.xml"
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
      "title": "DEFENSE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DEFENSE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disabling Enemy Flight Entry and Neutralizing Suspect Equipment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of Homeland Security or the Attorney General to deputize a State or local law enforcement officer to protect certain events with temporary flight restrictions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:41Z"
    }
  ]
}
```
