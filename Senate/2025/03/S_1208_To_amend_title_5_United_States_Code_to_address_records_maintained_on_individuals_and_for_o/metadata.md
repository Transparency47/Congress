# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1208?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1208
- Title: Privacy Act Modernization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1208
- Origin chamber: Senate
- Introduced date: 2025-03-31
- Update date: 2026-04-14T19:18:55Z
- Update date including text: 2026-04-14T19:18:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in Senate
- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-31: Introduced in Senate

## Actions

- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1208",
    "number": "1208",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Privacy Act Modernization Act of 2025",
    "type": "S",
    "updateDate": "2026-04-14T19:18:55Z",
    "updateDateIncludingText": "2026-04-14T19:18:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T20:53:37Z",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1208is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1208\nIN THE SENATE OF THE UNITED STATES\nMarch 31, 2025 Mr. Wyden (for himself, Mr. Markey , Mr. Merkley , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to address records maintained on individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Privacy Act Modernization Act of 2025 .\n#### 2. Modernizing Privacy Act definitions\n##### (a) Records\nSection 552a(a) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking a citizen of the United States or an alien lawfully admitted for permanent residence and inserting the following: \u201ca natural person who is\u2014\n(A) a United States person, as defined in section 101 of the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 ); or (B) in the United States; ;\n**(2)**\nby striking paragraphs (4) and (5) and inserting the following:\n(4) the term record means any personally identifiable information processed by an agency; (5) the term system of records means a group of any records maintained by or for, or otherwise under the control of, any agency; ;\n**(3)**\nin paragraph (12), by striking and at the end;\n**(4)**\nin paragraph (13), by striking the period at the end and inserting a semicolon; and\n**(5)**\nby adding at the end the following:\n(14) the term personally identifiable information means any information that identifies, or is linked or reasonably linkable, alone or in combination with other data, to\u2014 (A) an individual; or (B) a device that identifies, or is linked or reasonably linkable to, an individual; and (15) the term process , with respect to personally identifiable information, means to perform an operation or set of operations on the personally identifiable information, including by storing, analyzing, organizing, structuring, using, modifying, or otherwise handling the personally identifiable information, whether or not by automated means. .\n##### (b) Matching programs\nSection 552a(a)(8)(A) of title 5, United States Code, is amended\u2014\n**(1)**\nin the matter preceding clause (i), by striking of ;\n**(2)**\nin clause (i), in the matter preceding subclause (I), by striking two or more automated systems of records or a system of records with non-Federal records and inserting the following: involving any data from 1 or more systems of records ; and\n**(3)**\nin clause (ii), by striking two or more and inserting of 2 or more .\n##### (c) Government contractors\nSection 552a(m)(1) of title 5, United States Code, is amended by striking for the operation by or on behalf of the agency of a system of records to accomplish an agency function and inserting or other agreement, including with another agency, for the operation by or on behalf of the agency of a system of records .\n##### (d) Technical amendments\nSection 552a of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking section 552(e) and inserting section 552(f) ; and\n**(B)**\nin paragraph (8)(B)\u2014\n**(i)**\nin clause (iv)(III), by striking section 404(e), 464, or 1137 and inserting section 464 or 1137 ; and\n**(ii)**\nin clause (x), by striking section 3(d)(4) of the Achieving a Better Life Experience Act of 2014 and inserting section 529A(d)(4) of the Internal Revenue Code of 1986 ; and\n**(2)**\nin subsection (l), by striking National Archives of the United States each place that term appears and inserting National Archives and Records Administration .\n#### 3. Strengthening protections for individuals\n##### (a) Additional protections for collections, uses, and disclosures\nSection 552a of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(7), by inserting and is appropriate and reasonably necessary for the efficient and effective conduct of the Government before the semicolon at the end;\n**(2)**\nin subsection (b)(1), by inserting and that disclosure is consistent with, and related to, a purpose described under subsection (e)(4)(D) of this section before the semicolon at the end; and\n**(3)**\nin subsection (e)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking that maintains a system of records ;\n**(B)**\nin paragraph (2), by striking under Federal programs ;\n**(C)**\nin paragraph (4)\u2014\n**(i)**\nby amending subparagraph (D) to read as follows:\n(D) any purpose for which the information is intended to be used, including each routine use; ;\n**(ii)**\nin subparagraph (H), by striking and at the end;\n**(iii)**\nin subparagraph (I), by inserting and after the semicolon; and\n**(iv)**\nby adding at the end the following:\n(J) the legal authority for each purpose for which the records contained in the system are used, which shall contain a citation to the applicable law, executive order, or other authority; ;\n**(D)**\nin paragraph (11), by striking and at the end;\n**(E)**\nin paragraph (12), by striking the period at the end and inserting a semicolon; and\n**(F)**\nby adding at the end the following:\n(13) use records only for a legally authorized purpose; and (14) take reasonable efforts to ensure that a record that is disclosed contains the minimum amount of information necessary to accomplish the purpose of the disclosure. .\n##### (b) Additional protections for matching programs\nSection 552a(a)(8)(B) of title 5, United States Code, is amended\u2014\n**(1)**\nby amending clause (ii) to read as follows:\n(ii) matches performed to support any research or statistical project, if the results of the match are not intended to be used, and are not used, to\u2014 (I) make decisions concerning the rights, benefits, or privileges of specific individuals; or (II) take any adverse financial, personnel, or disciplinary action, or any other adverse action, against Federal personnel; ;\n**(2)**\nin clause (viii), by inserting or after the semicolon at the end;\n**(3)**\nby striking clause (ix); and\n**(4)**\nby redesignating clause (x) as clause (ix).\n##### (c) Additional civil remedies\nSection 552a(g) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby amending subparagraph (D) to read as follows:\n(D) fails to comply with any other provision of this section, or any rule promulgated thereunder, in such a way as to have, or that could reasonably lead to, an adverse effect on any person (including any State or territory (or any political subdivision of any State or territory) or any Indian Tribe), ; and\n**(B)**\nin the flush text following subparagraph (D), by inserting or person, as applicable, after the individual ; and\n**(2)**\nby amending paragraph (4) to read as follows:\n(4) In any suit brought under the provisions of subsection (g)(1)(C) or (D) of this section\u2014 (A) the court may provide such preliminary and other equitable or declaratory relief as may be appropriate; and (B) if the court determines that the agency acted in a manner that was intentional or willful, the United States shall be liable to the individual or person, as applicable, in an amount equal to the sum of\u2014 (i) actual damages, including nonpecuniary damages, sustained by the individual or person as a result of the refusal or failure, but in no case shall an individual or person entitled to recovery receive less than the sum of $1,000; (ii) the costs of the action together with reasonable attorney fees as determined by the court; and (iii) punitive damages in an amount determined appropriate by the court. .\n##### (d) Additional criminal penalties\nSection 552a(i) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by adding at the end the following: A person who commits an offense described in the previous sentence with the intent to sell, transfer, use, or disclose a record described in that sentence for commercial advantage, personal gain, or malicious harm shall be guilty of a felony and fined not more than $250,000, imprisoned for not more than 10 years, or both. ; and\n**(2)**\nin paragraph (3), by striking misdemeanor and fined not more than $5,000 and inserting felony and fined not more than $100,000 .\n#### 4. Effective dates\n##### (a) Definitions\nIn this section:\n**(1) Agency; matching program; recipient agency; record; source agency; system of records**\nThe terms agency , matching program , recipient agency , record , source agency , and system of records have the meanings given those terms in section 552a of title 5, United States Code, as amended by section 2.\n**(2) Special Government employee**\nThe term special Government employee has the meaning given the term in section 202(a) of title 18, United States Code.\n**(3) Temporary or intermittent expert or consultant**\nThe term temporary or intermittent expert or consultant means an expert or consultant or an organization thereof, the services of which are procured pursuant to section 3109 of title 5, United States Code.\n**(4) Temporary transitional Schedule C position**\nThe term temporary transitional Schedule C position means a position established under section 213.3302 of title 5, Code of Federal Regulations, or any successor regulation.\n##### (b) General effective date\nExcept as provided in subsection (c), the amendments made by sections 2 and 3 shall take effect on the date that is 2 years after the date of enactment of this Act.\n##### (c) Exceptions\nThe amendments made by sections 2 and 3 shall take effect on the date of enactment of this Act with respect to each of the following:\n**(1)**\nAny use of a record by, any disclosure of a record by or to, any maintenance of a system of records by or for, any control of a system of records by, the taking of any other action that is governed by section 552a of title 5, United States Code (as amended by this Act) by, or the taking of any of the preceding actions that is caused by any action by any of the following:\n**(A)**\nThe United States DOGE Service, or any successor organization.\n**(B)**\nThe U.S. DOGE Service Temporary Organization, or any successor organization.\n**(C)**\nAny special Government employee, any temporary or intermittent expert or consultant, or any individual occupying a temporary transitional Schedule C position.\n**(D)**\nAny agency not described in subparagraph (A) or (B) that is headed by, or subject to the control of\u2014\n**(i)**\nthe head of the entity described in subparagraph (A);\n**(ii)**\nthe head of the entity described in subparagraph (B); or\n**(iii)**\nany person described in subparagraph (C).\n**(E)**\nAny DOGE Team (as described in Executive Order 14158 (90 Fed. Reg. 8441), relating to establishing and implementing the President\u2019s Department of Government Efficiency ), or any successor organization.\n**(F)**\nAny agency that is within, or subject to the review of, an entity described in subparagraph (A), (B), (D), or (E).\n**(G)**\nAny officer, employee, expert, consultant, contractor, volunteer, or other individual, without regard to title or compensation, of, within, or providing services to an entity described in subparagraph (A), (B), (D), (E), or (F).\n**(2)**\nAny matching program in which\u2014\n**(A)**\nan entity or person described in any subparagraph of paragraph (1) is the source agency or recipient agency; or\n**(B)**\na system of records is maintained by or for, or otherwise under the control of, an entity or person described in any subparagraph of paragraph (1).\n##### (d) Applicability\nIf a person described in any subparagraph of paragraph (1) or (2) of subsection (c), outside of the capacity of the person as described in the applicable subparagraph, discloses a record, maintains a system of records, controls a system of records, participates in a matching program, takes any other action that is governed by section 552a of title 5, United States Code (as amended by this Act), or causes any other person to take any of the preceding actions, the exception under subsection (c) shall still apply with respect to that action by that person.\n#### 5. Rule of construction\n##### (a) Definition\nIn this section, the term Privacy Act means section 552a of title 5, United States Code, as in effect at any time before the date of enactment of this Act.\n##### (b) Rule\nNothing in this Act, or any amendment made by this Act, may be construed to create an inference with respect to the interpretation of any provision of the Privacy Act, any regulation promulgated under the Privacy Act, or any application of such a provision or regulation, including with respect to the scope of activity covered under the Privacy Act, the legality of any activity under the Privacy Act, or the availability of any remedy or award of damages with respect to a violation of the Privacy Act.",
      "versionDate": "2025-03-31",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-24T19:08:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119s1208",
          "measure-number": "1208",
          "measure-type": "s",
          "orig-publish-date": "2025-03-31",
          "originChamber": "SENATE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1208v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Privacy Act Modernization Act of 2025</strong></p><p>This bill strengthens privacy protections that apply to personal data held or maintained by government agencies. These\u00a0protections restrict the storage, access, use, and disclosure of personal data, such as an individual\u2019s name or Social Security number.</p><p>Currently, these protections apply to U.S. citizens and permanent residents. The bill expands this to include natural persons in the United States and certain associations and corporations.\u00a0</p><p>The bill places additional limits on the use and disclosure of such data, including by limiting the use of records to a legally authorized purpose and requiring disclosures to be minimal and consistent with a previously stated use.</p><p>The bill also increases existing penalties and creates additional criminal penalties for violations. For example, under the bill, an agency employee who willfully discloses individually identifiable information with the intent to sell, transfer, use, or disclose such information for commercial advantage, personal gain, or malicious harm shall be guilty of a felony and fined not more than $250,000, imprisoned for not more than 10 years, or both.</p><p>Courts may provide preliminary relief and, if the U.S. is found to have acted intentionally or willfully, the U.S. is\u00a0liable for additional types of damages (e.g., punitive).</p><p>The bill generally takes effect two years after the date of enactment. However, the bill takes effect immediately upon enactment with respect to certain actions taken by the Department of Government Efficiency (DOGE), certain special or temporary employees, and other related individuals and organizations.\u00a0</p>"
        },
        "title": "Privacy Act Modernization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1208.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Privacy Act Modernization Act of 2025</strong></p><p>This bill strengthens privacy protections that apply to personal data held or maintained by government agencies. These\u00a0protections restrict the storage, access, use, and disclosure of personal data, such as an individual\u2019s name or Social Security number.</p><p>Currently, these protections apply to U.S. citizens and permanent residents. The bill expands this to include natural persons in the United States and certain associations and corporations.\u00a0</p><p>The bill places additional limits on the use and disclosure of such data, including by limiting the use of records to a legally authorized purpose and requiring disclosures to be minimal and consistent with a previously stated use.</p><p>The bill also increases existing penalties and creates additional criminal penalties for violations. For example, under the bill, an agency employee who willfully discloses individually identifiable information with the intent to sell, transfer, use, or disclose such information for commercial advantage, personal gain, or malicious harm shall be guilty of a felony and fined not more than $250,000, imprisoned for not more than 10 years, or both.</p><p>Courts may provide preliminary relief and, if the U.S. is found to have acted intentionally or willfully, the U.S. is\u00a0liable for additional types of damages (e.g., punitive).</p><p>The bill generally takes effect two years after the date of enactment. However, the bill takes effect immediately upon enactment with respect to certain actions taken by the Department of Government Efficiency (DOGE), certain special or temporary employees, and other related individuals and organizations.\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119s1208"
    },
    "title": "Privacy Act Modernization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Privacy Act Modernization Act of 2025</strong></p><p>This bill strengthens privacy protections that apply to personal data held or maintained by government agencies. These\u00a0protections restrict the storage, access, use, and disclosure of personal data, such as an individual\u2019s name or Social Security number.</p><p>Currently, these protections apply to U.S. citizens and permanent residents. The bill expands this to include natural persons in the United States and certain associations and corporations.\u00a0</p><p>The bill places additional limits on the use and disclosure of such data, including by limiting the use of records to a legally authorized purpose and requiring disclosures to be minimal and consistent with a previously stated use.</p><p>The bill also increases existing penalties and creates additional criminal penalties for violations. For example, under the bill, an agency employee who willfully discloses individually identifiable information with the intent to sell, transfer, use, or disclose such information for commercial advantage, personal gain, or malicious harm shall be guilty of a felony and fined not more than $250,000, imprisoned for not more than 10 years, or both.</p><p>Courts may provide preliminary relief and, if the U.S. is found to have acted intentionally or willfully, the U.S. is\u00a0liable for additional types of damages (e.g., punitive).</p><p>The bill generally takes effect two years after the date of enactment. However, the bill takes effect immediately upon enactment with respect to certain actions taken by the Department of Government Efficiency (DOGE), certain special or temporary employees, and other related individuals and organizations.\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119s1208"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1208is.xml"
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
      "title": "Privacy Act Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Privacy Act Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to address records maintained on individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:48Z"
    }
  ]
}
```
