# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/802?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/802
- Title: Pay Our Coast Guard Act
- Congress: 119
- Bill type: S
- Bill number: 802
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-12-05T21:48:28Z
- Update date including text: 2025-12-05T21:48:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/802",
    "number": "802",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Pay Our Coast Guard Act",
    "type": "S",
    "updateDate": "2025-12-05T21:48:28Z",
    "updateDateIncludingText": "2025-12-05T21:48:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T20:40:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "WA"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "AK"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MS"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "WI"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "DE"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "AK"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-11",
      "state": "ME"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "FL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s802is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 802\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Cruz (for himself, Ms. Cantwell , Mr. Sullivan , Mr. Wicker , Ms. Baldwin , and Ms. Blunt Rochester ) introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nTo amend title 14, United States Code, to make appropriations for Coast Guard pay in the event an appropriations Act expires before the enactment of a new appropriations Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pay Our Coast Guard Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Coast Guard is a military service and a branch of the Armed Forces of the United States at all times regardless of whether it operates as a service in the Department of Homeland Security or as a service in the Navy.\n**(2)**\nNotwithstanding respective appropriations and except as otherwise provided in law, members of the Coast Guard should receive treatment equitable to that of other members of the Armed Forces with regard to pay and benefits.\n#### 3. Coast Guard pay; continuation\n##### (a) In general\nChapter 27 of title 14, United States Code, is amended by adding at the end the following:\n2780. Pay; continuation during lapse in appropriations (a) In general In the case of any period in which there is a Coast Guard-specific funding lapse, there are appropriated such sums as may be necessary\u2014 (1) to provide pay and allowances to military members of the Coast Guard, including the reserve component thereof, who perform active service or in-active-duty training during such period; (2) to provide pay and benefits to qualified civilian employees of the Coast Guard; (3) to provide pay and benefits to qualified contract employees of the Coast Guard; and (4) to provide for\u2014 (A) the payment of a death gratuity under sections 1475 through 1477 and 1489 of title 10, with respect to members of the Coast Guard; (B) the payment or reimbursement of authorized funeral travel and travel related to the dignified transfer of remains and unit memorial services under section 481f of title 37, with respect to members of the Coast Guard; and (C) the temporary continuation of a basic allowance of housing for dependents of members of the Coast Guard dying on active duty, as authorized by section 403(l) of title 37. (b) Coast Guard-Specific funding lapse For purposes of this section, a Coast Guard-specific funding lapse occurs in any case in which\u2014 (1) a general appropriation bill providing appropriations for the Coast Guard for a fiscal year is not enacted before the beginning of such fiscal year (and no joint resolution making continuing appropriations for the Coast Guard is in effect); and (2) a general appropriation bill providing appropriations for the Department of Defense for such fiscal year is enacted before the beginning of such fiscal year (or a joint resolution making continuing appropriations for the Department of Defense is in effect). (c) Termination Appropriations and funds made available and authority granted for any fiscal year for any purpose under subsection (a) shall be available until whichever of the following first occurs: (1) The enactment into law of an appropriation (including a continuing appropriation) for such purpose. (2) The enactment into law of the applicable regular or continuing appropriations resolution or other Act without any appropriation for such purpose. (3) The termination of availability of appropriations for the Department of Defense. (d) Rate for operations; applicability to appropriations Acts Appropriations made pursuant to this section shall be at a rate for operations and to the extent and manner that would be provided by the pertinent appropriations Act. (e) Charge to future appropriations Expenditures made pursuant to this section shall be charged to the applicable appropriation, fund, or authorization whenever a bill in which such applicable appropriation, fund, or authorization is enacted into law. (f) Apportionment Appropriations and funds made available by or authority granted under this section may be used without regard to the time limitations for submission and approval of apportionments set forth in section 1513 of title 31, but nothing in this section may be construed to waive any other provision of law governing the apportionment of funds. (g) Definitions In this section: (1) Qualified civilian employee The term qualified civilian employee means a civilian employee of the Coast Guard who the Commandant determines is\u2014 (A) providing support to members of the Coast Guard or another Armed Force; or (B) performing work as an excepted employee or an employee performing emergency work, as such terms are defined by the Office of Personnel Management. (2) Qualified contract employee of the Coast Guard The term qualified contract employee of the Coast Guard means an individual performing work under a contract who the Commandant determines is\u2014 (A) providing support to military members or qualified civilian employees of the Coast Guard or another Armed Force; or (B) required to perform work during a lapse in appropriations. .\n##### (b) Clerical amendment\nThe analysis for chapter 27 of title 14, United States Code, is amended by adding at the end the following:\n2780. Pay; continuation during lapse in appropriations. .",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-02-24",
        "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation."
      },
      "number": "1542",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pay Our Coast Guard Parity Act of 2025",
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
        "updateDate": "2025-05-15T15:16:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s802",
          "measure-number": "802",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s802v00",
            "update-date": "2025-05-15"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Pay Our Coast Guard Act</strong></p><p>This bill provides continuing appropriations to the Coast Guard for pay and benefits when there is a Coast Guard-specific funding lapse.</p><p>Under the bill, a\u00a0<em>Coast Guard-specific funding lapse</em> occurs when (1) a bill providing appropriations for the Coast Guard for a fiscal year has not been enacted before the beginning of that fiscal year, and no joint resolution providing continuing appropriations for the Coast Guard is in effect; and (2) a bill providing appropriations for the Department of Defense (DOD) for the fiscal year has been enacted before the beginning of the fiscal year, or a joint resolution providing continuing appropriation for DOD is in effect.\u00a0</p><p>If a Coast Guard-specific funding lapse occurs, the bill provides appropriations to the Coast Guard for</p><ul><li>pay and allowances for military members of the Coast Guard who perform active service or inactive-duty training;</li><li>pay and benefits for certain civilian employees and contract employees;</li><li>the payment of a death gratuity;</li><li>payments for travel related to funerals, the dignified transfer of remains, and unit memorial services; and</li><li>the temporary continuation of the basic allowance for housing for dependents of members of the Coast Guard dying on active duty.</li></ul><p>The bill generally provides the appropriations to the Coast Guard until the earlier of (1)\u00a0the enactment of specified Coast Guard appropriations legislation, or (2)\u00a0the termination of the availability of appropriations for DOD.</p>"
        },
        "title": "Pay Our Coast Guard Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s802.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Our Coast Guard Act</strong></p><p>This bill provides continuing appropriations to the Coast Guard for pay and benefits when there is a Coast Guard-specific funding lapse.</p><p>Under the bill, a\u00a0<em>Coast Guard-specific funding lapse</em> occurs when (1) a bill providing appropriations for the Coast Guard for a fiscal year has not been enacted before the beginning of that fiscal year, and no joint resolution providing continuing appropriations for the Coast Guard is in effect; and (2) a bill providing appropriations for the Department of Defense (DOD) for the fiscal year has been enacted before the beginning of the fiscal year, or a joint resolution providing continuing appropriation for DOD is in effect.\u00a0</p><p>If a Coast Guard-specific funding lapse occurs, the bill provides appropriations to the Coast Guard for</p><ul><li>pay and allowances for military members of the Coast Guard who perform active service or inactive-duty training;</li><li>pay and benefits for certain civilian employees and contract employees;</li><li>the payment of a death gratuity;</li><li>payments for travel related to funerals, the dignified transfer of remains, and unit memorial services; and</li><li>the temporary continuation of the basic allowance for housing for dependents of members of the Coast Guard dying on active duty.</li></ul><p>The bill generally provides the appropriations to the Coast Guard until the earlier of (1)\u00a0the enactment of specified Coast Guard appropriations legislation, or (2)\u00a0the termination of the availability of appropriations for DOD.</p>",
      "updateDate": "2025-05-15",
      "versionCode": "id119s802"
    },
    "title": "Pay Our Coast Guard Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Our Coast Guard Act</strong></p><p>This bill provides continuing appropriations to the Coast Guard for pay and benefits when there is a Coast Guard-specific funding lapse.</p><p>Under the bill, a\u00a0<em>Coast Guard-specific funding lapse</em> occurs when (1) a bill providing appropriations for the Coast Guard for a fiscal year has not been enacted before the beginning of that fiscal year, and no joint resolution providing continuing appropriations for the Coast Guard is in effect; and (2) a bill providing appropriations for the Department of Defense (DOD) for the fiscal year has been enacted before the beginning of the fiscal year, or a joint resolution providing continuing appropriation for DOD is in effect.\u00a0</p><p>If a Coast Guard-specific funding lapse occurs, the bill provides appropriations to the Coast Guard for</p><ul><li>pay and allowances for military members of the Coast Guard who perform active service or inactive-duty training;</li><li>pay and benefits for certain civilian employees and contract employees;</li><li>the payment of a death gratuity;</li><li>payments for travel related to funerals, the dignified transfer of remains, and unit memorial services; and</li><li>the temporary continuation of the basic allowance for housing for dependents of members of the Coast Guard dying on active duty.</li></ul><p>The bill generally provides the appropriations to the Coast Guard until the earlier of (1)\u00a0the enactment of specified Coast Guard appropriations legislation, or (2)\u00a0the termination of the availability of appropriations for DOD.</p>",
      "updateDate": "2025-05-15",
      "versionCode": "id119s802"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s802is.xml"
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
      "title": "Pay Our Coast Guard Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pay Our Coast Guard Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 14, United States Code, to make appropriations for Coast Guard pay in the event an appropriations Act expires before the enactment of a new appropriations Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T01:48:20Z"
    }
  ]
}
```
