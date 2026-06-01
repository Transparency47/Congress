# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1546?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1546
- Title: Patent Eligibility Restoration Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1546
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-01-22T19:16:28Z
- Update date including text: 2026-01-22T19:16:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1546",
    "number": "1546",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
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
    "title": "Patent Eligibility Restoration Act of 2025",
    "type": "S",
    "updateDate": "2026-01-22T19:16:28Z",
    "updateDateIncludingText": "2026-01-22T19:16:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T15:32:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sponsorshipDate": "2025-05-01",
      "state": "DE"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "TN"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1546is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1546\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Tillis (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Judiciary\nA BILL\nTo amend title 35, United States Code, to address matters relating to patent subject matter eligibility, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Patent Eligibility Restoration Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAs of the day before the date of enactment of this Act, patent eligibility jurisprudence interpreting section 101 of title 35, United States Code, requires significant modification and clarification.\n**(2)**\nFor many years after the original enactment of section 101 of title 35, United States Code, the Supreme Court of the United States and other courts created judicial exceptions to the wording of that section, thereby rendering an increasing number of inventions ineligible for patent protection.\n**(3)**\nEfforts by judges of district courts and courts of appeals of the United States to apply the exceptions described in paragraph (2) to specific circumstances have led to extensive confusion and a lack of consistency\u2014\n**(A)**\nthroughout the judicial branch of the Federal Government and Federal agencies; and\n**(B)**\namong patent practitioners.\n**(4)**\nMany judges of the United States Court of Appeals for the Federal Circuit and of various district courts of the United States have explicitly expressed the need for more guidance with respect to the meaning of section 101 of title 35, United States Code, and many patent owners, and persons that engage with patent owners, complain that the interpretation of that section is extremely confusing and difficult to discern and apply with any confidence.\n**(5)**\nUnder this Act, and the amendments made by this Act, the state of the law shall be as follows:\n**(A)**\nAll judicial exceptions to patent eligibility are eliminated.\n**(B)**\nAny invention or discovery that can be claimed as a useful process, machine, manufacture, or composition of matter, or any useful improvement thereof, is eligible for patent protection, except as explicitly provided in section 101 of title 35, United States Code, as amended by this Act, as described in subparagraphs (D) and (E) of this paragraph.\n**(C)**\nSections 102, 103, and 112 of title 35, United States Code, will continue to prescribe the requirements for obtaining a patent, but no such requirement will be used in determining patent eligibility.\n**(D)**\nThe following inventions shall not be eligible for patent protection:\n**(i)**\nA mathematical formula that is not part of an invention that is in a category described in subparagraph (B).\n**(ii)**\nA mental process performed solely in the mind of a human being.\n**(iii)**\nAn unmodified human gene, as that gene exists in the human body.\n**(iv)**\nAn unmodified human gene that is isolated from the human body, but otherwise the same as that gene exists in the human body.\n**(v)**\nAn unmodified natural material, as that material exists in nature.\n**(vi)**\nA process that is substantially economic, financial, business, social, cultural, or artistic.\n**(E)**\nUnder the exception described in subparagraph (D)(vi)\u2014\n**(i)**\nprocess claims drawn solely to the steps undertaken by human beings in methods of doing business, performing dance moves, offering marriage proposals, and the like shall not be eligible for patent coverage, and adding a non-essential reference to a computer by merely stating, for example, do it on a computer shall not establish such eligibility; and\n**(ii)**\nany process that cannot be practically performed without the use of a machine (including a computer) or manufacture shall be eligible for patent coverage.\n#### 3. Patent eligibility\n##### (a) In general\nChapter 10 of title 35, United States Code, is amended\u2014\n**(1)**\nin section 100\u2014\n**(A)**\nin subsection (b), by striking includes a new use of a known process and inserting includes a use, application, or method of manufacture of a known or naturally-occurring process ; and\n**(B)**\nby adding at the end the following:\n(k) The term useful means, with respect to an invention or discovery, that the invention or discovery has a specific and practical utility from the perspective of a person of ordinary skill in the art to which the invention or discovery pertains. ; and\n**(2)**\nby amending section 101 to read as follows:\n101. Patent eligibility (a) In general Whoever invents or discovers any useful process, machine, manufacture, or composition of matter, or any useful improvement thereof, may obtain a patent therefor, subject only to the exclusions in subsection (b) and to the further conditions and requirements of this title. (b) Eligibility exclusions (1) In general Subject to paragraph (2), a person may not obtain a patent for any of the following, if claimed as such: (A) A mathematical formula that is not part of a claimed invention in a category described in subsection (a). (B) A process that is substantially economic, financial, business, social, cultural, or artistic, even though at least 1 step in the process refers to a machine or manufacture. (C) A process that\u2014 (i) is a mental process performed solely in the human mind; or (ii) occurs in nature wholly independent of, and prior to, any human activity. (D) An unmodified human gene, as that gene exists in the human body. (E) An unmodified natural material, as that material exists in nature. (2) Conditions For the purposes of\u2014 (A) subparagraphs (A) and (B) of paragraph (1), the claimed invention shall not be excluded from eligibility for a patent if the invention cannot practically be performed without the use of a machine or manufacture; (B) paragraph (1)(D), a human gene shall not be considered to be unmodified if that human gene is\u2014 (i) purified, enriched, or otherwise altered by human activity; or (ii) otherwise employed in a useful invention or discovery; and (C) paragraph (1)(E), a natural material shall not be considered to be unmodified if that natural material is\u2014 (i) isolated, purified, enriched, or otherwise altered by human activity; or (ii) otherwise employed in a useful invention or discovery. (c) Eligibility (1) In general In determining whether, under this section, a claimed invention is eligible for a patent, eligibility shall be determined\u2014 (A) by considering the claimed invention as a whole and without discounting or disregarding any claim element; and (B) without regard to\u2014 (i) the manner in which the claimed invention was made; (ii) whether a claim element is known, conventional, routine, or naturally occurring; (iii) the state of the applicable art, as of the date on which the claimed invention is invented; or (iv) any other consideration in section 102, 103, or 112. (2) Infringement action (A) In general In an action brought for infringement under this title, the court, at any time, may determine whether an invention or discovery that is a subject of the action is eligible for a patent under this section, including on motion of a party when there are no genuine issues of material fact. (B) Limited discovery With respect to a determination described in subparagraph (A), the court may consider limited discovery relevant only to the eligibility described in that subparagraph before ruling on a motion described in that subparagraph. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 10 of title 35, United States Code, is amended by striking the item relating to section 101 and inserting the following:\n101. Patent eligibility. .\n#### 4. Rules of construction\n##### (a) Obviousness-Type double patenting\nNothing in this Act, or any amendment made by this Act, may be construed to affect or alter the judicially-created doctrine of obviousness-type double patenting.\n##### (b) Insignificant extra-Solution activity\nWith respect to the exclusions to patent eligibility described in subparagraphs (A) and (B) of section 101(b)(1) of title 35, United States Code, as added by section 3 of this Act, the inclusion of pre- or post-solution activity by a computer (or other machine or manufacture) in claim language shall not be sufficient to confer patent eligibility on the claim if that computer (or other machine or manufacture) is not necessary to practically perform the invention.",
      "versionDate": "",
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
        "actionDate": "2025-05-01",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3152",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Patent Eligibility Restoration Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Intellectual property",
            "updateDate": "2025-09-03T20:19:39Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-09-03T20:19:39Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-09-03T20:19:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-22T13:12:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
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
          "measure-id": "id119s1546",
          "measure-number": "1546",
          "measure-type": "s",
          "orig-publish-date": "2025-05-01",
          "originChamber": "SENATE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1546v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Patent Eligibility Restoration Act of 2025</strong></p><p>This bill amends the law relating to patent subject matter eligibility to establish that only specified subject matter (e.g., a natural process wholly independent of human activity) is ineligible for patenting. (Currently, subject matter eligibility is determined by examining whether the claimed invention is directed to certain ineligible categories, and if so, whether there is an inventive concept. Subject matter eligibility is one of several requirements that an invention must satisfy in order to receive patent protection.)</p><p>Under this bill, an invention shall be considered to involve patent-ineligible subject matter only if it falls within specified categories, such as (1) a mathematical formula that is not part of a useful process, machine, manufacture, or composition; (2) a mental process that is performed solely in the human mind; or (3) an unmodified human gene as the gene exists in the human body.</p>"
        },
        "title": "Patent Eligibility Restoration Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1546.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Patent Eligibility Restoration Act of 2025</strong></p><p>This bill amends the law relating to patent subject matter eligibility to establish that only specified subject matter (e.g., a natural process wholly independent of human activity) is ineligible for patenting. (Currently, subject matter eligibility is determined by examining whether the claimed invention is directed to certain ineligible categories, and if so, whether there is an inventive concept. Subject matter eligibility is one of several requirements that an invention must satisfy in order to receive patent protection.)</p><p>Under this bill, an invention shall be considered to involve patent-ineligible subject matter only if it falls within specified categories, such as (1) a mathematical formula that is not part of a useful process, machine, manufacture, or composition; (2) a mental process that is performed solely in the human mind; or (3) an unmodified human gene as the gene exists in the human body.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119s1546"
    },
    "title": "Patent Eligibility Restoration Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Patent Eligibility Restoration Act of 2025</strong></p><p>This bill amends the law relating to patent subject matter eligibility to establish that only specified subject matter (e.g., a natural process wholly independent of human activity) is ineligible for patenting. (Currently, subject matter eligibility is determined by examining whether the claimed invention is directed to certain ineligible categories, and if so, whether there is an inventive concept. Subject matter eligibility is one of several requirements that an invention must satisfy in order to receive patent protection.)</p><p>Under this bill, an invention shall be considered to involve patent-ineligible subject matter only if it falls within specified categories, such as (1) a mathematical formula that is not part of a useful process, machine, manufacture, or composition; (2) a mental process that is performed solely in the human mind; or (3) an unmodified human gene as the gene exists in the human body.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119s1546"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1546is.xml"
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
      "title": "Patent Eligibility Restoration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Patent Eligibility Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 35, United States Code, to address matters relating to patent subject matter eligibility, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:37Z"
    }
  ]
}
```
