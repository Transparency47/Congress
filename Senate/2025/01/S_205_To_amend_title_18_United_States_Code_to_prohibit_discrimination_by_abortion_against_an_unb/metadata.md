# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/205?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/205
- Title: Protecting Individuals with Down Syndrome Act
- Congress: 119
- Bill type: S
- Bill number: 205
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-03-13T11:03:17Z
- Update date including text: 2026-03-13T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/205",
    "number": "205",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Protecting Individuals with Down Syndrome Act",
    "type": "S",
    "updateDate": "2026-03-13T11:03:17Z",
    "updateDateIncludingText": "2026-03-13T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
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
            "date": "2025-01-23T17:20:47Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-23T17:20:47Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OK"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ND"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AR"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MO"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MS"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NE"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s205is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 205\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Daines (for himself, Mr. Lankford , Mr. Risch , Mr. Cramer , Mr. Budd , Mr. Banks , Mr. Boozman , Mrs. Hyde-Smith , Mrs. Britt , Mr. Hawley , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit discrimination by abortion against an unborn child on the basis of Down syndrome.\n#### 1. Short title\nThis Act may be cited as the Protecting Individuals with Down Syndrome Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOn June 24, 2022, the United States Supreme Court issued a decision in Dobbs v. Jackson Women\u2019s Health Organization (No. 19\u20131392, 2022 WL 2276808 (2022)), which overturned its prior, egregiously wrong holding in Roe v. Wade (410 U.S. 113 (1973)).\n**(2)**\nDobbs correctly affirmed that there is no constitutional right to abort an unborn child and that the Court\u2019s prior decision in Roe was not based in the Constitution\u2019s text nor was it deeply rooted in the history and tradition of the United States.\n**(3)**\nFederal law protects individuals with disabilities against discrimination, including in the provision of medical care.\n**(4)**\nAs Congress has previously affirmed, [d]isability is a natural part of the human experience and in no way diminishes the right of individuals to live independently, enjoy self-determination, make choices, contribute to society, pursue meaningful careers, and enjoy full inclusion and integration in the economic, political, social, and educational mainstream of American society.\n**(5)**\nIt is the policy of the United States to respect the lives and the dignity of individuals with disabilities, including individuals with Down syndrome.\n**(6)**\nFederal, State, and local government all have a role to play in preventing discrimination based on disability, including discrimination against individuals with Down syndrome.\n**(7)**\nConsistent with the overarching Federal policy of nondiscrimination, and in light of the shameful history of targeting unborn children for abortion based on race, gender, or disabilities, Congress must combat invidious discrimination by prohibiting doctors from aborting unborn children because the unborn child has been diagnosed with Down syndrome.\n**(8)**\nTragically, in some countries that have failed to protect unborn children diagnosed with Down syndrome, virtually every unborn child diagnosed with Down syndrome is aborted.\n**(9)**\nIndividuals with Down syndrome are inherently valuable and worthy of dignity and respect. They enrich and strengthen our society in countless ways, including but not limited to building meaningful relationships, participating in and creating families, learning, and working alongside other Americans.\n#### 3. Discrimination by abortion against an unborn child on the basis of Down syndrome prohibited\n##### (a) In general\nChapter 13 of title 18, United States Code, is amended by adding at the end the following:\n251. Discrimination by abortion against an unborn child on the basis of Down syndrome prohibited (a) Definitions In this section: (1) Abortion The term abortion means the act of using or prescribing any instrument, medicine, drug, or any other substance, device, or means with the intent to\u2014 (A) kill the unborn child of a woman known to be pregnant; or (B) terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) to produce a live birth and preserve the life and health of the child born alive; (ii) to save the life of the pregnant woman; or (iii) to remove a dead unborn child. (2) Down syndrome The term Down syndrome means a chromosomal disorder associated with\u2014 (A) an extra copy of the chromosome 21, in whole or in part; or (B) an effective trisomy for chromosome 21. (3) Qualified plaintiff The term qualified plaintiff means\u2014 (A) a woman upon whom an abortion is performed or attempted in violation of this section; (B) a maternal grandparent of the unborn child if the woman upon whom an abortion is performed or attempted in violation of this section is an unemancipated minor; (C) the father of an unborn child who is the subject of an abortion performed or attempted in violation of this section unless the pregnancy or abortion resulted from the criminal conduct of the father; or (D) the Attorney General. (4) Unborn child The term unborn child means an individual of the species homo sapiens from the beginning of the biological development of that individual, including fertilization, until the point of being born alive, as defined in section 8(b) of title 1. (b) Offense It shall be unlawful to\u2014 (1) perform an abortion\u2014 (A) with the knowledge that a pregnant woman is seeking an abortion, in whole or in part, on the basis of\u2014 (i) a test result indicating that the unborn child has Down syndrome; (ii) a prenatal diagnosis that the unborn child has Down syndrome; or (iii) any other reason to believe that the unborn child has or may have Down syndrome; or (B) without first\u2014 (i) asking the pregnant woman if she is aware of any test results, prenatal diagnosis, or any other evidence that the unborn child has or may have Down syndrome; and (ii) if the woman is aware that the unborn child has or may have Down syndrome, informing the pregnant woman of the prohibitions on abortion under this section; (2) use force or the threat of force to intentionally injure or intimidate any person for the purpose of coercing an abortion described in paragraph (1)(A); (3) solicit or accept funds for the performance of an abortion described in paragraph (1)(A); or (4) knowingly transport a woman into the United States or across a State line for the purpose of obtaining an abortion described in paragraph (1)(A). (c) Criminal penalty Any person that violates, or attempts to violate, subsection (b) shall be fined under this title, imprisoned not more than 5 years, or both. (d) Civil remedies (1) Civil action by woman on whom abortion is performed A woman upon whom an abortion has been performed or attempted in violation of subsection (b)(2) may bring a civil action in an appropriate court against any person who engaged in a violation of subsection (b)(2) to obtain appropriate relief. (2) Civil action by relatives (A) In general Except as provided in subparagraph (B), the father of an unborn child who is the subject of an abortion performed or attempted in violation of subsection (b), or a maternal grandparent of the unborn child if the pregnant woman is an unemancipated minor, may bring a civil action in an appropriate court against any person who engaged in the violation to obtain appropriate relief. (B) Exceptions Subparagraph (A) shall not apply if\u2014 (i) the pregnancy or abortion resulted from the criminal conduct of the plaintiff described in subparagraph (A); or (ii) the plaintiff described in subparagraph (A) consented to the abortion. (3) Appropriate relief Appropriate relief in a civil action under this subsection includes\u2014 (A) objectively verifiable money damages for all injuries, psychological and physical, including loss of companionship and support, occasioned by the violation of this section; and (B) punitive damages. (4) Injunctive relief A qualified plaintiff may bring a civil action in an appropriate court to obtain injunctive relief to prevent an abortion provider from performing or attempting further abortions in violation of this section. (5) Attorney\u2019s fees for plaintiff The court shall award a reasonable attorney\u2019s fee as part of the costs to a prevailing plaintiff in a civil action under this subsection. (e) Bar to prosecution A woman upon whom an abortion is performed may not be prosecuted or held civilly liable for any violation of this section or for a conspiracy to violate this section. (f) Loss of Federal funding A violation of subsection (b) shall be deemed discrimination for the purposes of section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ). (g) Reporting requirement (1) In general A physician, physician\u2019s assistant, nurse, counselor, or other medical or mental health professional shall report known or suspected violations of any of this section to appropriate law enforcement authorities. (2) Criminal penalty Any person who violates paragraph (1) shall be fined under this title, imprisoned not more than 1 year, or both. (h) Expedited consideration It shall be the duty of the district courts of the United States, the courts of appeals of the United States, and the Supreme Court of the United States to advance on the docket and to expedite to the greatest possible extent the disposition of any matter brought under this section. (i) Protection of privacy in court proceedings (1) In general Except to the extent the Constitution of the United States or other similarly compelling reason requires, in every civil or criminal action under this section, the court shall make such orders as are necessary to protect the anonymity of any woman upon whom an abortion has been performed or attempted if she does not give her written consent to such disclosure. Such orders may be made upon motion, but shall be made sua sponte if not otherwise sought by a party. (2) Orders to parties, witnesses, and counsel The court shall issue appropriate orders to the parties, witnesses, and counsel and shall direct the sealing of the record and exclusion of individuals from courtrooms or hearing rooms to the extent necessary to safeguard the identity of a woman described in paragraph (1) from public disclosure. (3) Pseudonym required In the absence of written consent of the woman upon whom an abortion has been performed or attempted, any party, other than a public official, who brings an action under this section shall do so under a pseudonym. (4) Limitation This subsection may not be construed to conceal the identity of the plaintiff or of witnesses from the defendant or from attorneys for the defendant. (j) Rule of construction (1) Greater protection Nothing in this section may be construed to pre-empt or limit any Federal, State or local law that provides greater protections for an unborn child than those provided in this section. (2) Creating or recognizing right Nothing in this section shall be construed as creating or recognizing a right to abortion nor shall it make lawful an abortion that is otherwise unlawful under Federal, State, or local law. .\n##### (b) Clerical amendment\nThe table of sections of chapter 13 of title 18, United States Code, is amended by adding at the end the following:\n251. Discrimination by abortion against an unborn child on the basis of Down syndrome prohibited. .\n#### 4. Severability\nIf any portion of this Act, or the amendments made by this Act, or the application thereof to any person or circumstance is held invalid, such invalidity shall not affect the portions or applications of this Act which can be given effect without the invalid portion or application.",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-03-21",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2251",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Individuals with Down Syndrome Act",
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
            "name": "Abortion",
            "updateDate": "2025-03-21T18:45:13Z"
          },
          {
            "name": "Birth defects",
            "updateDate": "2025-03-21T18:45:13Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-21T18:45:13Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-03-21T18:45:13Z"
          },
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2025-03-21T18:45:13Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-03-21T18:45:13Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-21T18:45:13Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-03-21T18:45:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-24T14:38:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s205",
          "measure-number": "205",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s205v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Protecting Individuals with Down Syndrome Act</b></p> <p> This bill creates new federal crimes related to the performance of an abortion on an unborn child who has Down syndrome.</p> <p>It subjects a violator to criminal penalties\u2014a fine, a prison term of up to five years, or both.</p> <p>It also authorizes civil remedies, including damages and injunctive relief.</p> <p>A woman who undergoes such an abortion may not be prosecuted or held civilly liable.</p>"
        },
        "title": "Protecting Individuals with Down Syndrome Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s205.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Protecting Individuals with Down Syndrome Act</b></p> <p> This bill creates new federal crimes related to the performance of an abortion on an unborn child who has Down syndrome.</p> <p>It subjects a violator to criminal penalties\u2014a fine, a prison term of up to five years, or both.</p> <p>It also authorizes civil remedies, including damages and injunctive relief.</p> <p>A woman who undergoes such an abortion may not be prosecuted or held civilly liable.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s205"
    },
    "title": "Protecting Individuals with Down Syndrome Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Protecting Individuals with Down Syndrome Act</b></p> <p> This bill creates new federal crimes related to the performance of an abortion on an unborn child who has Down syndrome.</p> <p>It subjects a violator to criminal penalties\u2014a fine, a prison term of up to five years, or both.</p> <p>It also authorizes civil remedies, including damages and injunctive relief.</p> <p>A woman who undergoes such an abortion may not be prosecuted or held civilly liable.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s205"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s205is.xml"
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
      "title": "Protecting Individuals with Down Syndrome Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Individuals with Down Syndrome Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to prohibit discrimination by abortion against an unborn child on the basis of Down syndrome.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:19Z"
    }
  ]
}
```
