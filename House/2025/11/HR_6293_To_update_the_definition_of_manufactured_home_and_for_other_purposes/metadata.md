# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6293?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6293
- Title: Housing Supply Expansion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6293
- Origin chamber: House
- Introduced date: 2025-11-25
- Update date: 2026-03-18T08:06:48Z
- Update date including text: 2026-03-18T08:06:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-25: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-25: Introduced in House

## Actions

- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-25",
    "latestAction": {
      "actionDate": "2025-11-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6293",
    "number": "6293",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000612",
        "district": "6",
        "firstName": "John",
        "fullName": "Rep. Rose, John W. [R-TN-6]",
        "lastName": "Rose",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Housing Supply Expansion Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-18T08:06:48Z",
    "updateDateIncludingText": "2026-03-18T08:06:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-25",
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
          "date": "2025-11-25T16:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NE"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "MO"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "CA"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "TX"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "IA"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "NC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "VA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NH"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6293ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6293\nIN THE HOUSE OF REPRESENTATIVES\nNovember 25, 2025 Mr. Rose (for himself, Mr. Flood , Mr. Cleaver , Mr. Peters , Ms. De La Cruz , and Mr. Correa ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo update the definition of manufactured home, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Supply Expansion Act of 2025 .\n#### 2. Updating the definition of manufactured home\n##### (a) In general\nSection 603(6) of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402(6) ) is amended by striking on a permanent chassis and inserting with or without a permanent chassis .\n##### (b) Standards for manufactured homes built without a permanent chassis\nSection 604(a) of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5403 ) is amended by adding at the end the following:\n(7) Standards for manufactured homes built without a permanent chassis (A) In general The Secretary shall issue revised standards for manufactured homes built without a permanent chassis and shall consult with the consensus committee in the development of such, using the process described in paragraph (4). (B) Creating final standards The Secretary shall, after consulting and conferring with the consensus committee, establish standards to include manufactured homes without a permanent chassis have\u2014 (i) a distinct label to be issued by the Secretary distinguishing manufactured homes built without a permanent chassis from manufactured homes built on a permanent chassis; (ii) a data plate, as described in section 3280.5 of title 24, Code of Federal Regulations, distinguishing manufactured homes built without a permanent chassis from manufactured homes built on a permanent chassis; and (iii) a notation on any invoice produced by the manufacturer of a manufactured home that is distinguishable from the invoice for a manufactured home constructed with a permanent chassis. .\n##### (c) Manufactured home standards and certifications\nSection 604 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5403 ) is amended by adding at the end the following:\n(i) Manufactured home standards and certifications (1) In general (A) Initial certification Subject to subparagraph (B), not later than 1 year after the date of enactment of the Housing Supply Expansion Act of 2025 , a State shall submit to the Secretary an initial certification that the laws and regulations of the State\u2014 (i) treat a manufactured home, including a manufactured home without a permanent chassis, in parity with a manufactured home (as defined and regulated by the State); and (ii) subject a manufactured home without a permanent chassis to the same laws and regulations of the State as a manufactured home built on a permanent chassis with respect to financing, title, insurance, manufacture, sale, taxes, transportation, installation, and other areas as the secretary determines, after consultation with and approval by the consensus committee, are necessary to give effect to the purpose of this section. (B) State plan submission Any State plan submitted under subparagraph (C) shall contain the required State certification under subparagraph (A) or paragraph (3) and, if contained therein, no additional or State certification under subparagraph (A) or paragraph (3). (C) Extended deadline With respect to a State with a legislature that meets biennially, the deadline for the submission of the initial certification required under subparagraph (A) shall be 2 years after the date of enactment of the Housing Supply Expansion Act of 2025 . (D) Late certification (i) No waiver The Secretary may not waive the prohibition described in paragraph (5)(B) with respect to a certification submitted after the deadline under subparagraph (A) or paragraph (3) unless the Secretary approves the late certification. (ii) Rule of construction Nothing in this subsection shall be construed to prevent a State from submitting the initial certification required under subparagraph (A) after the required deadline under that subparagraph. (2) Form of State certification not presented in a State plan The initial certification required under paragraph (1)(A), if not submitted with a State plan under paragraph (1)(B), shall contain, in a form prescribed by the Secretary, an attestation by an official that the State has taken the steps necessary to ensure the veracity of the certification required under paragraph (1)(A), including, as necessary, by\u2014 (A) amending the definition of manufactured home in the laws and regulations of the State; and (B) directing State agencies to amend the definition of manufactured home in regulations. (3) Annual recertification Not later than a date to be determined by the Secretary each year, a State shall submit to the Secretary an additional certification that\u2014 (A) confirms the accuracy of the initial certification submitted under subparagraph (A) or (B) of paragraph (1); and (B) certifies that any new laws or regulations enacted or adopted by the State since the date of the previous certification does not change the veracity of the initial certification submitted under paragraph (1)(A). (4) List The Secretary shall publish and maintain in the Federal Register and on the website of the Department of Housing and Urban Development a list of States that are up-to-date with the submission of initial and subsequent certifications required under this subsection. (5) Prohibition (A) Definition In this paragraph, the term covered manufactured home means a home that is\u2014 (i) not considered a manufactured home under the laws and regulations of a State because the home is constructed without a permanent chassis; (ii) considered a manufactured home under the definition of the term in section 603; and (iii) constructed after the date of enactment of the Housing Supply Expansion Act of 2025 . (B) Building, installation, and sale If a State does not submit a certification under paragraph (1)(A) or (3) by the date on which those certifications are required to be submitted\u2014 (i) with respect to a State in which the State administers the installation of manufactured homes, the State shall prohibit the manufacture, installation, or sale of a covered manufactured home within the State; and (ii) with respect to a State in which the Secretary administers the installation of manufactured homes, the State and the Secretary shall prohibit the manufacture, installation, or sale of a covered manufactured home within the State. .\n##### (d) Other Federal laws regulating manufactured homes\nThe Secretary of Housing and Urban Development may coordinate with the heads of other Federal agencies to ensure that Federal agencies treat a manufactured home (as defined in Federal laws and regulations other than section 603 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402 )) in the same manner as a manufactured home (as defined in section 603 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402 )), as amended by this Act.\n##### (e) Assistance to States\nSection 609 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5408 ) is amended\u2014\n**(1)**\nin paragraph (1), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) model guidance to support the submission of the certification required under section 604(i). .\n##### (f) Preemption\nNothing in this section or the amendments made by this section shall be construed as limiting the scope of Federal preemption under section 604(d) of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5403(d) ).",
      "versionDate": "2025-11-25",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-23",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2414",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Housing Supply Expansion Act of 2025",
      "type": "S"
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
        "updateDate": "2025-12-03T13:46:49Z"
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
      "date": "2025-11-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6293ih.xml"
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
      "title": "Housing Supply Expansion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T11:08:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Supply Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-02T11:08:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To update the definition of manufactured home, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-02T11:03:25Z"
    }
  ]
}
```
