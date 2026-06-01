# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6462?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6462
- Title: Rural Recovery Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6462
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-16T08:07:01Z
- Update date including text: 2026-05-16T08:07:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H5040)
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H5040)
- 2026-01-13 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6462",
    "number": "6462",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001232",
        "district": "6",
        "firstName": "April",
        "fullName": "Rep. McClain Delaney, April [D-MD-6]",
        "lastName": "McClain Delaney",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Rural Recovery Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:01Z",
    "updateDateIncludingText": "2026-05-16T08:07:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H5040)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:04:22Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "CO"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "OR"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NM"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6462ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6462\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mrs. McClain Delaney (for herself, Mr. Evans of Colorado , Ms. Salinas , Ms. Stansbury , and Mr. Thompson of California ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo direct the Secretary of Agriculture to establish a program to provide to rural communities technical assistance in recovering from disasters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Recovery Act of 2025 .\n#### 2. Rural development disaster recovery technical assistance program\n##### (a) Definitions\nIn this section:\n**(1) Disaster**\nThe term disaster means a major disaster declared by the President under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ).\n**(2) Eligible rural community**\nThe term eligible rural community means each rural community all or part of which is within an area covered by a disaster.\n**(3) Program**\nThe term program means the program established under subsection (b).\n**(4) Rural community**\n**(A) In general**\nSubject to subparagraph (B), the term rural community means any census designated place with a population of less than 20,000.\n**(B) Modification; waiver**\nThe Secretary may, as the Secretary determines to be necessary\u2014\n**(i)**\nmodify the definition of rural community under subparagraph (A); or\n**(ii)**\nwaive the applicability of the definition of rural community under this paragraph to a particular area.\n**(5) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) Establishment\nThe Secretary shall establish within the rural development mission area a program to provide technical assistance for eligible rural communities.\n##### (c) Providers of technical assistance\n**(1) In general**\nTechnical assistance under the program shall be provided by\u2014\n**(A)**\na State office of the rural development mission area;\n**(B)**\nan entity described in paragraph (2) that enters into a contract with a State office of the rural development mission area; or\n**(C)**\nboth entities described in subparagraphs (A) and (B).\n**(2) Eligibility of contractors**\n**(A) In general**\nAn entity eligible to enter into a contract under paragraph (1)(B) is a public body or private nonprofit corporation described in section 306(a)(26)(A) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a)(26)(A) ).\n**(B) Priority**\nIn entering into contracts under paragraph (1)(B), the Secretary shall give priority to entities described in section 306(a)(26)(B) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a)(26)(B) ).\n**(3) Coordination**\nA provider of technical assistance under the program shall, to the extent practicable, coordinate with State governments and local stakeholders to ensure the equitable distribution of outreach to eligible rural communities.\n##### (d) Requirements of technical assistance\nA provider of technical assistance under the program shall provide technical assistance to eligible rural communities relating to disaster recovery\u2014\n**(1)**\nincluding assistance in\u2014\n**(A)**\nplanning, and identifying issues, potential solutions, and sources of funding, with respect to disaster recovery;\n**(B)**\npreparing and submitting applications with respect to assistance for disaster recovery to Federal agencies, such as the Economic Development Administration, the Federal Emergency Management Agency, and the rural development mission area, and State agencies;\n**(C)**\naddressing denials of applications described in subparagraph (B); and\n**(D)**\nimplementing funding received for disaster recovery from Federal agencies and State agencies described in subparagraph (B); and\n**(2)**\nwhich may involve\u2014\n**(A)**\ntelecommunications;\n**(B)**\nwater infrastructure;\n**(C)**\nhousing;\n**(D)**\nenergy infrastructure;\n**(E)**\ncommunity facilities;\n**(F)**\nbusiness infrastructure; and\n**(G)**\nlocal government infrastructure.\n##### (e) Duration\n**(1) In general**\nAn eligible rural community may receive technical assistance under the program during the 3-year period beginning on the date on which a disaster is declared for the area within which all or part of the eligible rural community lies.\n**(2) Extension**\nThe Secretary may extend the period of eligibility described in paragraph (1) for an additional 3-year period with respect to an eligible rural community on a case-by-case basis.\n##### (f) Multiple recipients\nMore than 1 eligible rural community all or part of which are within an area covered by a disaster may receive technical assistance under the program.\n##### (g) Funding\n**(1) Provision**\nAs soon as practicable after the date on which a disaster is declared for the area within which all or part of an eligible rural community lies, the Secretary shall make available to the applicable State office of the rural development mission area amounts available to carry out this section, without any requirement for the submission of an application by such State office.\n**(2) Allocation**\nThe Secretary shall allocate amounts made available to carry out this section for each fiscal year to eligible rural communities in accordance with a formula established by the Secretary that is based on the population of individuals affected by a disaster, as determined using data from the most recent decennial census.\n##### (h) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $50,000,000 for each fiscal year.",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-07-15",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "2281",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Rural Recovery Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-07T16:03:58Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6462ih.xml"
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
      "title": "Rural Recovery Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Recovery Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to establish a program to provide to rural communities technical assistance in recovering from disasters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:33:22Z"
    }
  ]
}
```
