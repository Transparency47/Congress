# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/987?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/987
- Title: Protecting Life and Integrity in Research Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 987
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-12-05T21:50:51Z
- Update date including text: 2025-12-05T21:50:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/987",
    "number": "987",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Protecting Life and Integrity in Research Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:50:51Z",
    "updateDateIncludingText": "2025-12-05T21:50:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T17:48:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "ID"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "OK"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "LA"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "MO"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "OK"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "MT"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "WY"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "UT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "ND"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s987is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 987\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mrs. Hyde-Smith (for herself, Mr. Risch , Mr. Lankford , Mr. Kennedy , Mr. Hawley , Mr. Mullin , Mr. Daines , Mr. Barrasso , Mr. Lee , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit the Federal Government from conducting, funding, approving, or otherwise supporting any research involving human fetal tissue that is obtained pursuant to an induced abortion, and to prohibit the solicitation or knowing acquisition, receipt, or acceptance of a donation of such tissue.\n#### 1. Short title\nThis Act may be cited as the Protecting Life and Integrity in Research Act of 2025 .\n#### 2. No research involving human fetal tissue obtained pursuant to an induced abortion\n##### (a) In general\n**(1) In general**\nNo Federal department, agency, or office may conduct, fund, approve, or otherwise support any research involving human fetal tissue that is obtained pursuant to an induced abortion.\n**(2) Development of new, ethical cell lines**\nSubsection (a) does not limit the authority of the head of any Federal department, agency, or office, to develop or support the development of new, high-efficiency cell lines, including for the production of vaccines and genetic vectors, so long as the cell lines are not derived from human fetal tissue that is obtained pursuant to an induced abortion.\n**(3) Research involving human fetal tissue obtained after a miscarriage or stillbirth permitted**\nAny research of any Federal department, agency, or office on human fetal tissue obtained after a miscarriage or stillbirth shall be conducted or supported in accordance with section 498A of the Public Health Service Act ( 42 U.S.C. 289g\u20131 ).\n**(4) Definition**\nIn this subsection, the term human fetal tissue has the meaning given such term in section 498A(g) of the Public Health Service Act ( 42 U.S.C. 289g\u20131(g) ).\n##### (b) Amendments to the PHSA limiting human fetal tissue research to tissue obtained after a miscarriage or stillbirth\nSection 498A of the Public Health Service Act ( 42 U.S.C. 289g\u20131 ) is amended\u2014\n**(1)**\nin the section heading, by striking transplantation of fetal tissue and inserting human fetal tissue obtained after a miscarriage or stillbirth ;\n**(2)**\nby amending subsection (a) to read as follows:\n(a) Establishment of program The Secretary may conduct or support research on human fetal tissue obtained after a miscarriage or a stillbirth. ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(B), by inserting if the human fetal tissue is intended for transplantation, before the donation ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking subparagraph (A); and\n**(ii)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (A) and (B), respectively;\n**(4)**\nin subsection (c)(1)(B), by striking pursuant to a spontaneous or induced abortion or pursuant to and inserting after a miscarriage or ; and\n**(5)**\nby amending subsection (g) to read as follows:\n(g) Definitions In this section: (1) Human fetal tissue The term human fetal tissue means tissue or cells obtained from a dead unborn child pursuant to an induced abortion, a miscarriage, or a stillbirth. (2) Miscarriage The term miscarriage means the involuntary death of an unborn child who was carried in the womb for a period of less than 20 weeks. (3) Stillbirth The term stillbirth means the involuntary death of an unborn child who was carried in the womb for a period of 20 weeks or more. (4) Unborn child -The term unborn child has the meaning given such term in section 1841(d) of title 18, United States Code. .\n##### (c) Conforming repeal\nSection 113 of the National Institutes of Health Revitalization Act of 1993 ( 42 U.S.C. 289g\u20131 note) is repealed.\n#### 3. Prohibition against solicitation or knowing acquisition, receipt, or acceptance of a donation of human fetal tissue knowing that the tissue was obtained pursuant to an induced abortion\n##### (a) In general\nParagraph (1) of section 498B(c) of the Public Health Service Act ( 42 U.S.C. 289g\u20132(c) ) is amended to read as follows:\n(1) solicit or knowingly acquire, receive, or accept a donation (excluding any transfer for purposes of autopsy or burial) of human fetal tissue knowing that\u2014 (A) a human pregnancy was deliberately initiated to provide such tissue; or (B) the tissue was obtained pursuant to an induced abortion; or .\n##### (b) Conforming changes\nSection 498B of the Public Health Service Act ( 42 U.S.C. 289g\u20132 ) is amended\u2014\n**(1)**\nby striking subsection (b);\n**(2)**\nby redesignating subsections (c) through (e) as subsections (b) through (d), respectively; and\n**(3)**\nin subsection (c), as redesignated\u2014\n**(A)**\nin paragraph (1), by striking (a), (b), or (c) and inserting (a) or (b) ; and\n**(B)**\nin paragraph (2), by striking or (b)(3) .",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2075",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Life and Integrity in Research Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-03-31T15:03:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119s987",
          "measure-number": "987",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2025-09-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s987v00",
            "update-date": "2025-09-08"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Life and Integrity in Research Act of 2025</strong></p><p>This bill prohibits federal agencies from supporting research involving, and prohibits any entity from soliciting or knowingly acquiring, human fetal tissue obtained pursuant to an induced abortion.\u00a0</p><p>Specifically, the bill prohibits any federal agency from conducting, funding, approving, or otherwise supporting research involving such tissue. Federal agencies may conduct or support research involving human fetal tissue obtained after a miscarriage or stillbirth.</p><p>Additionally, the bill prohibits any entity from soliciting or knowingly acquiring, receiving, or accepting a donation of human fetal tissue where the entity knows it was obtained pursuant to an induced abortion. Entities violating this prohibition are subject to criminal penalties. The bill provides an exception for transfers for purposes of autopsy or burial.</p>"
        },
        "title": "Protecting Life and Integrity in Research Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s987.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Life and Integrity in Research Act of 2025</strong></p><p>This bill prohibits federal agencies from supporting research involving, and prohibits any entity from soliciting or knowingly acquiring, human fetal tissue obtained pursuant to an induced abortion.\u00a0</p><p>Specifically, the bill prohibits any federal agency from conducting, funding, approving, or otherwise supporting research involving such tissue. Federal agencies may conduct or support research involving human fetal tissue obtained after a miscarriage or stillbirth.</p><p>Additionally, the bill prohibits any entity from soliciting or knowingly acquiring, receiving, or accepting a donation of human fetal tissue where the entity knows it was obtained pursuant to an induced abortion. Entities violating this prohibition are subject to criminal penalties. The bill provides an exception for transfers for purposes of autopsy or burial.</p>",
      "updateDate": "2025-09-08",
      "versionCode": "id119s987"
    },
    "title": "Protecting Life and Integrity in Research Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Life and Integrity in Research Act of 2025</strong></p><p>This bill prohibits federal agencies from supporting research involving, and prohibits any entity from soliciting or knowingly acquiring, human fetal tissue obtained pursuant to an induced abortion.\u00a0</p><p>Specifically, the bill prohibits any federal agency from conducting, funding, approving, or otherwise supporting research involving such tissue. Federal agencies may conduct or support research involving human fetal tissue obtained after a miscarriage or stillbirth.</p><p>Additionally, the bill prohibits any entity from soliciting or knowingly acquiring, receiving, or accepting a donation of human fetal tissue where the entity knows it was obtained pursuant to an induced abortion. Entities violating this prohibition are subject to criminal penalties. The bill provides an exception for transfers for purposes of autopsy or burial.</p>",
      "updateDate": "2025-09-08",
      "versionCode": "id119s987"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s987is.xml"
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
      "title": "Protecting Life and Integrity in Research Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-04T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Life and Integrity in Research Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Federal Government from conducting, funding, approving, or otherwise supporting any research involving human fetal tissue that is obtained pursuant to an induced abortion, and to prohibit the solicitation or knowing acquisition, receipt, or acceptance of a donation of such issue.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:02Z"
    }
  ]
}
```
