# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4441?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4441
- Title: CREATE AI Act
- Congress: 119
- Bill type: S
- Bill number: 4441
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-18T20:14:26Z
- Update date including text: 2026-05-18T20:14:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-04-29: Introduced in Senate

## Actions

- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4441",
    "number": "4441",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "CREATE AI Act",
    "type": "S",
    "updateDate": "2026-05-18T20:14:26Z",
    "updateDateIncludingText": "2026-05-18T20:14:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T20:58:14Z",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NM"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "SD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NJ"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4441is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4441\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Young (for himself, Mr. Heinrich , Mr. Rounds , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish the National Artificial Intelligence Research Resource, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Creating Resources for Every American To Experiment with Artificial Intelligence Act or the CREATE AI Act .\n#### 2. National Artificial Intelligence Research Resource\n##### (a) In general\nThe National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 et seq. ) is amended by adding at the end the following:\nLVI National Artificial Intelligence Research Resource Sec. 5601. Definitions. Sec. 5602. Establishment; governance. Sec. 5603. Resources of the NAIRR. Sec. 5604. NAIRR processes and procedures. 5601. Definitions In this title: (1) Executive agency The term Executive agency has the meaning given such term in section 105 of title 5, United States Code. (2) National Artificial Intelligence Research Resource; NAIRR The terms National Artificial Intelligence Research Resource and NAIRR have the meaning given the term National Artificial Intelligence Research Resource in section 5106(g). (3) Program management office The term Program Management Office means the Program Management Office established under section 5602(c). (4) Resource of the NAIRR The term resource of the NAIRR means a resource described in section 5603(1). 5602. Establishment; governance (a) Establishment Not later than 1 year after the date of enactment of the Creating Resources for Every American To Experiment with Artificial Intelligence Act , the Director of the National Science Foundation shall establish the National Artificial Intelligence Research Resource to\u2014 (1) advance artificial intelligence research and research that employs artificial intelligence; and (2) develop artificial intelligence skills for the United States workforce. (b) Function The function of the NAIRR shall be to connect United States researchers and educators to computational, data, software, and educational resources, provided by Executive agencies, State governments, or nongovernmental entities. (c) Program Management Office (1) Establishment The Director of the National Science Foundation shall\u2014 (A) establish within the Office of Advanced Cyberinfrastructure (or a successor office) of the National Science Foundation a Program Management Office to oversee the functions of the NAIRR; and (B) appoint an individual to head the Program Management Office. (2) Duties The duties of the Program Management Office shall include\u2014 (A) developing the budget for the NAIRR; (B) as needed, and with appropriate oversight, delegating operational tasks to 1 or more nongovernmental organizations that shall be selected through a competitive and transparent process; (C) coordinating resource contributions from participating Executive agencies, State governments, and nongovernmental entities; and (D) establishing policies and procedures for the NAIRR that carry out all requirements of section 5604. (d) Reporting The Director of the National Science Foundation shall develop, and make publicly available, an annual report on the progress of the NAIRR. 5603. Resources of the NAIRR The head of the Program Management Office shall\u2014 (1) coordinate and provision resources of the NAIRR, which shall include computational resources, data, software, models, testbeds, and educational resources; (2) establish processes to manage the acquisition and integration of new resources of the NAIRR, and intake of in-kind contribution of resources of the NAIRR, from Executive agencies, State governments, or nongovernmental entities; and (3) publicly report a summary of categories of available resources of the NAIRR. 5604. NAIRR processes and procedures (a) User eligibility (1) Eligible users Subject to paragraph (3), the following users shall be eligible for access to the NAIRR: (A) A researcher, educator, or student based in the United States that is affiliated with an entity described in paragraph (2). (B) An employee of an entity described in subclause (III) or (IV) of paragraph (2)(A)(ii) with a demonstrable mission-need. (2) Entities described An entity described in this paragraph is one of the following: (A) An entity that\u2014 (i) is based in the United States; and (ii) is\u2014 (I) an institution of higher education (as such term is defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )); (II) a nonprofit institution (as such term is defined in section 4 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3703 )); (III) an Executive agency, Congress, an agency of the legislative branch, or an agency of the judicial branch; (IV) a federally funded research and development center; (V) a small business concern (as such term is defined in section 3 of the Small Business Act ( 15 U.S.C. 632 ), notwithstanding section 121.103 of title 13, Code of Federal Regulations) that has received funding from an Executive agency, including through the Small Business Innovation Research Program or the Small Business Technology Transfer Program (as described in section 9 of the Small Business Act ( 15 U.S.C. 638 )); or (VI) a consortium composed of entities described in subclauses (I) through (V). (B) An entity that is determined to be eligible by the Director of the National Science Foundation and the Director of the Office of Science and Technology Policy. (3) Excluded entities (A) In general No individual is authorized to be an eligible user under paragraph (1) if the individual is employed by a foreign country that is listed in section 4872(f)(2) of title 10, United States Code, or is otherwise authorized by such country to act for or on its behalf. (B) Enforcement The Director of the National Science Foundation shall ensure that individuals authorized as eligible users meet the requirements of subparagraph (A). (4) User access selection The head of the Program Management Office shall establish an application process for eligible users to request access to the NAIRR. (b) Research security The head of the Program Management Office shall\u2014 (1) ensure conformance with the requirements of National Security Presidential Memorandum-33 (relating to supported research and development national policy), issued January 2021, and its implementation guidance on research security and research integrity, or any successor policy document or guidance; and (2) (A) designate a member of the Program Management Office as a research security point of contact with responsibility for overseeing conformance with National Security Presidential Memorandum-33 and its implementation guidance, or any successor policy document or guidance; and (B) if the head of the Program Management Office delegates responsibilities to another entity under section 5602(c)(2)(B), require the entity to designate a member of the leadership team for such entity to serve as a research security point of contact as described in subparagraph (A), with respect to the delegated responsibilities. (c) Open source The head of the Program Management Office shall establish policies to encourage software developed to administer the NAIRR, and software developed using resources of the NAIRR, to be open-source. (d) Fee schedule (1) In general The head of the Program Management Office may establish a fee schedule for access to the NAIRR. Access to the NAIRR may only require a fee if the fee is assessed according to such fee schedule. Such fee schedule\u2014 (A) may differ by type of eligible user and type of affiliated entity described in subsection (a); (B) shall include a free tier of access based on available funds and anticipated costs and demand; (C) may include cost-based charges for specified eligible users; and (D) shall ensure that the primary purpose of the NAIRR is to support research. (2) Retention and use of funds (A) Retaining of funds Notwithstanding section 3302 of title 31, United States Code, the head of the Program Management Office may retain fees collected under this subsection. (B) Availability and use of funds Amounts retained under subparagraph (A) shall\u2014 (i) remain available until expended; and (ii) be available to the head of the Program Management Office, without further appropriation, for the purposes of this title. (e) Advanced cyberinfrastructure advisory committee (1) In general The Director of the National Science Foundation shall establish an advisory committee to assess, and make recommendations regarding, the activities of the Office of Advanced Cyberinfrastructure, including the management of the NAIRR. (2) Members The membership requirements for the committee established under paragraph (1) shall be the same as the membership requirements described in section 10386(b) of the Research and Development, Innovation, and Competition Act ( 42 U.S.C. 19106(b) ). (3) Nonapplicability of FACA Chapter 10 of title 5, United States Code, shall not apply to the committee established under paragraph (1). .\n##### (b) Conforming amendments\nThe table of contents in section 2(b) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 134 Stat. 3388) is amended by inserting after the items relating to title LV the following:\nTITLE LVI\u2014National Artificial Intelligence Research Resource Sec. 5601. Definitions. Sec. 5602. Establishment; governance. Sec. 5603. Resources of the NAIRR. Sec. 5604. NAIRR processes and procedures. .",
      "versionDate": "2026-04-29",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-05-18T20:14:25Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4441is.xml"
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
      "title": "CREATE AI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T02:38:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CREATE AI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Creating Resources for Every American To Experiment with Artificial Intelligence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the National Artificial Intelligence Research Resource, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:36Z"
    }
  ]
}
```
