# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2755?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2755
- Title: Protecting American Research and Talent Act
- Congress: 119
- Bill type: S
- Bill number: 2755
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2025-12-05T21:55:55Z
- Update date including text: 2025-12-05T21:55:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2755",
    "number": "2755",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
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
    "title": "Protecting American Research and Talent Act",
    "type": "S",
    "updateDate": "2025-12-05T21:55:55Z",
    "updateDateIncludingText": "2025-12-05T21:55:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T17:19:11Z",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "OK"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "TX"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2755is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2755\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Mr. Cotton (for himself, Mr. Scott of Florida , Mr. Mullin , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo provide that no Federal funds may be obligated or expended to award a grant or contract to an institution of higher education for the specific purposes of conducting fundamental research in collaboration with a covered entity.\n#### 1. Short title\nThis Act may be cited as the Protecting American Research and Talent Act .\n#### 2. Prohibition on availability of funds for fundamental research collaboration with covered entities\n##### (a) Prohibition\nExcept as provided in subsection (b), no Federal funds may be obligated or expended to award a grant or contract to an institution of higher education for the specific purposes of conducting fundamental research in collaboration with a covered entity.\n##### (b) Waiver\n**(1) In general**\nThe head of a Federal agency may waive the prohibition described in subsection (a) on a case-by-case basis, with respect to an individual grant or contract with an eligible institution of higher education described in paragraph (2) if the agency head determines that such a waiver is in the national security interests of the United States.\n**(2) Eligibility**\n**(A) In general**\nAn institution of higher education is eligible for a waiver under this subsection if\u2014\n**(i)**\nthe international enrollment rate at the institution is less than 15 percent; and\n**(ii)**\nthe enrollment at the institution of students from foreign countries of concern is less than 5 percent of the international student body at the institution.\n**(B) Persecuted groups not to be included in cap**\n**(i) In general**\nFor purposes of calculating the enrollment at an institution of higher education of students under clauses (i) and (ii) of subparagraph (A), a student from a foreign country of concern who is member of a group on the list described in clause (ii) for such foreign country of concern shall not count toward the caps provided in such subparagraph.\n**(ii) List**\nThe Secretary of State shall establish a list for each foreign country of concern of groups who are the target of persecution in the foreign country of concern.\n**(3) Congressional notice**\nNot later than 30 days after the date on which an award is made by a Federal agency involving an institution of higher education with respect to which a waiver is made under paragraph (1), the head of the agency shall submit to Congress a notice of such waiver.\n##### (c) Report\n**(1) In general**\nOn an annual basis, each head of a Federal agency shall submit to Congress a report on the compliance of the agency and institutions of higher education with the requirements of this section.\n**(2) Contents**\nEach report annex submitted pursuant to paragraph (1) shall include\u2014\n**(A)**\na list of institutions of higher education that applied for funding that also applied for a waiver under subsection (b) during the period covered by the report, and for each of these institutions, statistics on domestic, international, and foreign country of concern enrollment in each of the institution's undergraduate and graduate schools; and\n**(B)**\nfor each waiver made under subsection (b) during the period covered by the report\u2014\n**(i)**\na justification for the waiver; and\n**(ii)**\na detailed description of the type and extent of any collaboration between an institution of higher education and a covered entity allowed pursuant to the waiver, including identification of the institution of higher education and the covered entity involved, the type of technology involved, the duration of the collaboration, and terms and conditions on intellectual property assignment, as applicable, under the collaboration agreement.\n##### (d) Definitions\nIn this Act:\n**(1) Collaboration**\nThe term collaboration means coordinated activity between an institution of higher education and a covered entity, and includes\u2014\n**(A)**\nsharing of research facilities, resources, or data;\n**(B)**\nsharing of technical know-how;\n**(C)**\nany financial or in-kind contribution intended to produce a research product;\n**(D)**\nsponsorship or facilitation of research fellowships, visas, or residence permits;\n**(E)**\njoint ventures, partnerships, or other formalized agreements for the purpose of conducting research or sharing resources, data, or technology;\n**(F)**\ninclusion of researchers as consultants, advisors, or members of advisory or review boards; and\n**(G)**\nsuch other activities as may be determined by the Secretary of Defense.\n**(2) Covered entity**\nThe term covered entity \u2014\n**(A)**\nmeans\u2014\n**(i)**\nany academic institution that is included in the most recently updated list developed pursuant to section 1286(c)(9) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. 4001 note);\n**(ii)**\nany entity included in the list of Chinese military companies operating in the United States most recently submitted under section 1260H(b)(1) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note); or\n**(iii)**\nany college or university in the People\u2019s Republic of China that\u2014\n**(I)**\nis known as the Seven Sons of National Defense ;\n**(II)**\nis designated under the Double First-Class Construction plan;\n**(III)**\nis designated or overseen by the State Administration for Science, Technology, and Industry for National Defense to host joint construction programs; or\n**(IV)**\notherwise conducts research or other activities in support of implementation of military-civil fusion strategy or national defense capabilities; and\n**(B)**\nincludes\u2014\n**(i)**\nany individual employed by, or receiving funding from, an entity or academic institution described in subparagraph (A);\n**(ii)**\nany foreign person who holds a degree from an academic institution described in subparagraph (A); and\n**(iii)**\nany foreign person who receives funding from\u2014\n**(I)**\nan entity described in subparagraph (A);\n**(II)**\na foreign talent program included in the most recently updated list developed pursuant to section 1286(c)(10) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. 4001 note); or\n**(III)**\na foreign country of concern or an entity based in a foreign country of concern, whether or not directly sponsored by the foreign country of concern.\n**(3) Foreign country of concern**\nThe term foreign country of concern has the meaning given the term in section 10612(a) of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; 136 Stat. 1635; 42 U.S.C. 19221 ) .\n**(4) Fundamental research**\nThe term fundamental research has the meaning given that term in National Security Decision Directive\u2013189 (NSSD\u2013189), National Policy on the Transfer of Scientific, Technical and Engineering Information, dated September 21, 1985, or any successor document.\n**(5) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ) and includes\u2014\n**(A)**\nany department, program, project, faculty, researcher, or other individual, entity, or activity of such institution; and\n**(B)**\nany branch of such institution within or outside the United States.",
      "versionDate": "2025-09-10",
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
        "actionDate": "2025-09-10",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "5253",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting American Research and Talent Act",
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
        "name": "Education",
        "updateDate": "2025-09-23T16:12:01Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2755is.xml"
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
      "title": "Protecting American Research and Talent Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T11:03:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting American Research and Talent Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide that no Federal funds may be obligated or expended to award a grant or contract to an institution of higher education for the specific purposes of conducting fundamental research in collaboration with a covered entity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:19Z"
    }
  ]
}
```
