# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3866?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3866
- Title: A bill to provide for updates to the Federal Aviation Administration type certification process to support development of new and novel technologies, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 3866
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-03-09T18:39:57Z
- Update date including text: 2026-03-09T18:39:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3866",
    "number": "3866",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "A bill to provide for updates to the Federal Aviation Administration type certification process to support development of new and novel technologies, and for other purposes.",
    "type": "S",
    "updateDate": "2026-03-09T18:39:57Z",
    "updateDateIncludingText": "2026-03-09T18:39:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T19:19:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "UT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NM"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "WY"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "MT"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "KS"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "IN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3866is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3866\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Welch (for himself, Mr. Budd , Mr. Curtis , Mr. Luj\u00e1n , Ms. Lummis , Mr. Sheehy , Mr. Moran , Mr. Young , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo provide for updates to the Federal Aviation Administration type certification process to support development of new and novel technologies, and for other purposes.\n#### 1. Table of contents\n##### (a) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Table of contents.\nSec. 2. Transparency of the FAA type certification process.\nSec. 3. Criteria for FAA issue papers.\nSec. 4. FAA delegation guidance.\n#### 2. Transparency of the FAA type certification process\n##### (a) In general\nTo support innovation in aviation and the development of new and novel technologies and to ensure global leadership in aviation, not later than 180 days after the date of enactment of this section, the Administrator shall publish on the official website of the FAA a publicly available plan for\u2014\n**(1)**\nimproving the issue paper process associated with applications for a type certificate or supplemental type certificate under section 44704 of title 49, United States Code;\n**(2)**\ndetermining, in any given certification project, the maximum extent possible to which an industry consensus standard can be used as an acceptable means or method of compliance, to the extent consistent with the public interest in aviation safety, and in the Administrator\u2019s sole discretion;\n**(3)**\ncreating stable policy, to the extent practicable, regarding subjects that the Administrator determines are commonly addressed in issue papers, special conditions, special airworthiness criteria, or findings on equivalent levels of safety; and\n**(4)**\nensuring consideration of performance-based standards when promulgating requirements applicable to the type certification of aircraft, aircraft engine, or propeller.\n##### (b) Standard expected timelines\nNot later than 270 days after the date of enactment of this section, and subject to subsection (c), the Administrator shall amend FAA order 8110.112A (or any successor document), and shall make conforming amendments to other applicable FAA orders and related documents, to establish a range of standard expected timelines for\u2014\n**(1)**\nachievement of major milestones established in the type certification process, including the development of issue papers and memoranda regarding certification basis, certification plan means of compliance, and equivalent levels of safety, including the anticipated FAA response time at applicable stages of the issue paper process;\n**(2)**\nthe amount of time that passes between\u2014\n**(A)**\nclosure of an issue paper that contains a special condition; and\n**(B)**\npublication of the respective notice of proposed rulemaking and final rule regarding such special condition, if the FAA decides to publish a proposed special condition;\n**(3)**\nresponses by the Administrator to\u2014\n**(A)**\napplicant petitions for exemptions; and\n**(B)**\napplicant proposals setting forth means of compliance with applicable performance-based design standards; and\n**(4)**\nsubstantive responses by an applicant to the Administrator\u2019s requests for information the Administrator deems necessary to close out petitions and proposals covered under paragraph (3).\n##### (c) Exclusion\nSubsection (b) shall not apply with respect to complex issues that, in the Administrator\u2019s sole determination, present an unsafe condition.\n##### (d) Consultation requirement\nIn carrying out the requirements under subsections (a) and (b), the Administrator shall consult with\u2014\n**(1)**\ntrade associations and advanced air mobility stakeholders that represent prior and prospective applicants for type certificates, including, but not limited to, type certificates for powered-lift or other aircraft designed for operation in advanced air mobility use cases;\n**(2)**\ntrade associations and prospective infrastructure providers that represent airports or vertiports that serve the aircraft covered where the certification process would require changes to the infrastructure design of such airports or vertiports;\n**(3)**\nthe certified bargaining representatives of aviation safety inspectors, aviation safety specialists, technicians, and engineers of the Administration; and\n**(4)**\nany other relevant organizations and stakeholders, as determined by the Administrator.\n##### (e) Report to Congress\nNot later than 180 days after the Administrator establishes standard expected timelines under subsection (b), and annually thereafter, the Administrator, in consultation with the FAA\u2019s Executive Director of the Aircraft Certification Service, shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives, a report on the status of the implementation of this section, including\u2014\n**(1)**\nmetrics on the FAA\u2019s performance in meeting standard expected timelines under subsection (b);\n**(2)**\na description of processes under which the Administrator reviews internal performance and addresses deficiencies as needed;\n**(3)**\ndetails on any instance where standard expected timelines were exceeded and changes to staffing levels, administration, processes, or capabilities that could improve performance to align with standard expected timelines; and\n**(4)**\nthe Administrator\u2019s progress in creating stable policy with respect to matters commonly covered in issue papers.\n#### 3. Criteria for FAA issue papers\n##### (a) In general\nTo support the FAA type certification process, and therefore innovation in aviation, including the development of new and novel technologies related to advanced air mobility, and to ensure global leadership in aviation, not later than 180 days after the date of enactment of this section, the Administrator shall amend FAA order 8110.112A (or a successor document) and other applicable FAA documents to\u2014\n**(1)**\ninclude specific criteria to be used to determine\u2014\n**(A)**\nwhen an issue is so significant that it rises to the level that it warrants the establishment of an issue paper; and\n**(B)**\nwhich roles within the FAA will be responsible for evaluating whether each criterion is met;\n**(2)**\naccount for performance-based rule projects that require issue papers regarding both means and methods of compliance; and\n**(3)**\nimprove efficiency and timelines by eliminating recurring issue papers by\u2014\n**(A)**\nconverting stable means of compliance issue papers into published policy or advisory circulars; and\n**(B)**\nincorporating stable issue papers for special conditions, exemptions, equivalent level of safety findings, and other requirements through annual updates to product airworthiness standards issued under title 14, Code of Federal Regulations.\n##### (b) Subsequent orders\nIn the event such FAA order 8110.112A is superseded or canceled, the Administrator shall ensure that the matters described in paragraphs (1), (2), and (3) of subsection (a) are included in a subsequent order governing issue papers.\n#### 4. FAA delegation guidance\n##### (a) In general\nNot later than 90 days after the date of enactment of this section, the Administrator shall publish on the official website of the FAA updated delegation guidance for type certification of aircraft and aircraft engines under section 44704(a) of title 49, United States Code.\n##### (b) Requirements\nThe updated delegation guidance required by subsection (a) shall include each of the following:\n**(1)**\nCriteria for applicant eligibility for delegation.\n**(2)**\nCriteria for classification of compliance findings that are considered routine and those that are considered safety-critical.\n**(3)**\nProcesses for documentation and management review when FAA elects not to use authorized representatives of the Administrator or the applicant to perform routine and type certification activities.\n**(4)**\nThe extent to which the FAA\u2019s implementation of delegation authority considers how to ensure safety and foster predictable and routine type certification processes for new and novel technologies.\n**(5)**\nThe extent to which the FAA\u2019s implementation of delegation authority considers how a type certification process, as described in paragraph (4), impacts United States global leadership in the development and production of these technologies.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3885",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Aviation Innovation and Global Competitiveness Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-12",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "7553",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Aviation Innovation and Global Competitiveness Act",
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
        "updateDate": "2026-03-04T15:42:54Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3866is.xml"
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
      "title": "A bill to provide for updates to the Federal Aviation Administration type certification process to support development of new and novel technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-03T06:18:21Z"
    },
    {
      "title": "A bill to provide for updates to the Federal Aviation Administration type certification process to support development of new and novel technologies, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T11:56:28Z"
    }
  ]
}
```
