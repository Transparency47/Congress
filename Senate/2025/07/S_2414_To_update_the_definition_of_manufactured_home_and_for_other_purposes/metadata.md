# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2414?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2414
- Title: Housing Supply Expansion Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2414
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2026-02-27T12:03:21Z
- Update date including text: 2026-02-27T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2414",
    "number": "2414",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Housing Supply Expansion Act of 2025",
    "type": "S",
    "updateDate": "2026-02-27T12:03:21Z",
    "updateDateIncludingText": "2026-02-27T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
            "date": "2025-07-23T19:54:37Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-23T19:54:37Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "AZ"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "SC"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "HI"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "AL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "ID"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "AZ"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NH"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2414is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2414\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Tillis (for himself, Mr. Gallego , Mr. Scott of South Carolina , Mr. Schatz , Mrs. Britt , Mr. Padilla , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo update the definition of manufactured home, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Supply Expansion Act of 2025 .\n#### 2. Updating the definition of manufactured home\n##### (a) In general\nSection 603(6) of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402(6) ) is amended by striking on a permanent chassis and inserting with or without a permanent chassis .\n##### (b) Manufactured home certifications\nSection 604 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5403 ) is amended by adding at the end the following:\n(i) Manufactured home certifications (1) In general (A) Initial certification Subject to subparagraph (B), not later than 1 year after the date of enactment of the Housing Supply Expansion Act of 2025 , a State shall submit to the Secretary an initial certification that the laws and regulations of the State\u2014 (i) treat a manufactured home, including a manufactured home without a permanent chassis, in parity with a manufactured home (as defined and regulated by the State); and (ii) subject a manufactured home without a permanent chassis to the same laws and regulations of the State as a manufactured home built on a permanent chassis with respect to financing, title, insurance, manufacture, sale, taxes, transportation, installation, and other areas as the secretary determines, after consultation with and approval by the consensus committee, are necessary to give effect to the purpose of this section. (B) State plan submission Any State plan submitted under subparagraph (C) shall contain the required State certification under subparagraph (A) or paragraph (3) and, if contained therein, no additional or State certification under subparagraph (A) or paragraph (3). (C) Extended deadline With respect to a State with a legislature that meets biennially, the deadline for the submission of the initial certification required under subparagraph (A) shall be 2 years after the date of enactment of the Housing Supply Expansion Act of 2025 . (D) Late certification (i) No waiver The Secretary may not waive the prohibition described in paragraph (5)(B) with respect to a certification submitted after the deadline under subparagraph (A) or paragraph (3) unless the Secretary approves the late certification. (ii) Rule of construction Nothing in this subsection shall be construed to prevent a State from submitting the initial certification required under subparagraph (A) after the required deadline under that subparagraph. (2) Form of State certification not presented in a State plan The initial certification required under paragraph (1)(A), if not submitted with a State plan under paragraph (1)(B), shall contain, in a form prescribed by the Secretary, an attestation by an official that the State has taken the steps necessary to ensure the veracity of the certification required under paragraph (1)(A), including, as necessary, by\u2014 (A) amending the definition of manufactured home in the laws and regulations of the State; and (B) directing State agencies to amend the definition of manufactured home in regulations. (3) Annual recertification Not later than a date to be determined by the Secretary each year, a State shall submit to the Secretary an additional certification that\u2014 (A) confirms the accuracy of the initial certification submitted under subparagraph (A) or (B) of paragraph (1); and (B) certifies that any new laws or regulations enacted or adopted by the State since the date of the previous certification does not change the veracity of the initial certification submitted under paragraph (1)(A). (4) List The Secretary shall publish and maintain in the Federal Register and on the website of the Department of Housing and Urban Development a list of States that are up-to-date with the submission of initial and subsequent certifications required under this subsection. (5) Prohibition (A) Definition In this paragraph, the term covered manufactured home means a home that is\u2014 (i) not considered a manufactured home under the laws and regulations of a State because the home is constructed without a permanent chassis; (ii) considered a manufactured home under the definition of the term in section 603; and (iii) constructed after the date of enactment of the Housing Supply Expansion Act of 2025 . (B) Building, installation, and sale If a State does not submit a certification under paragraph (1)(A) or (3) by the date on which those certifications are required to be submitted\u2014 (i) with respect to a State in which the State administers the installation of manufactured homes, the State shall prohibit the manufacture, installation, or sale of a covered manufactured home within the State; and (ii) with respect to a State in which the Secretary administers the installation of manufactured homes, the State and the Secretary shall prohibit the manufacture, installation, or sale of a covered manufactured home within the State. .\n##### (c) Other Federal laws regulating manufactured homes\nThe Secretary of Housing and Urban Development may coordinate with the heads of other Federal agencies to ensure that Federal agencies treat a manufactured home (as defined in Federal laws and regulations other than section 603 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402 )) in the same manner as a manufactured home (as defined in section 603 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402 )), as amended by this Act.\n##### (d) Assistance to States\nSection 609 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5408 ) is amended\u2014\n**(1)**\nin paragraph (1), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) model guidance to support the submission of the certification required under section 604(i). .\n##### (e) Preemption\nNothing in this section or the amendments made by this section shall be construed as limiting the scope of Federal preemption under section 604(d) of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5403(d) ).",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-08-01",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 143."
      },
      "number": "2651",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ROAD to Housing Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-25",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "6293",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Housing Supply Expansion Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-12T16:27:01Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2414is.xml"
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
      "title": "Housing Supply Expansion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-27T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Housing Supply Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to update the definition of manufactured home, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:22Z"
    }
  ]
}
```
