# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1949?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1949
- Title: Combating Violent and Dangerous Crime Act
- Congress: 119
- Bill type: S
- Bill number: 1949
- Origin chamber: Senate
- Introduced date: 2025-06-04
- Update date: 2026-04-17T15:22:34Z
- Update date including text: 2026-04-17T15:22:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-04: Introduced in Senate
- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-04: Introduced in Senate

## Actions

- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1949",
    "number": "1949",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Combating Violent and Dangerous Crime Act",
    "type": "S",
    "updateDate": "2026-04-17T15:22:34Z",
    "updateDateIncludingText": "2026-04-17T15:22:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-04",
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
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T21:21:22Z",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "AR"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "ND"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "LA"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "OK"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "KY"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "ME"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "WV"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "ID"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NC"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "ID"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1949is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1949\nIN THE SENATE OF THE UNITED STATES\nJune 4, 2025 Mr. Grassley (for himself, Mr. Boozman , Mr. Cramer , Mr. Cassidy , Mr. Lankford , Mr. McConnell , Ms. Collins , Mrs. Capito , Mr. Crapo , Mr. Tillis , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo improve certain criminal provisions.\n#### 1. Short title\nThis Act may be cited as the Combating Violent and Dangerous Crime Act .\n#### 2. Bank robbery and related crimes\nSection 2113 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking , or attempts to take, ;\n**(B)**\nby striking or attempts to obtain ; and\n**(C)**\nby inserting before ; or the following: , or attempts to do so ;\n**(2)**\nby redesignating subsections (f), (g), and (h) as subsections (g), (h), and (i), respectively; and\n**(3)**\nby inserting after subsection (e) the following:\n(f) Whoever conspires to commit any offense under this section shall be subject to the same penalties as those prescribed for the offense the commission of which was the object of the conspiracy. .\n#### 3. Protection of officers and employees of the United States\n##### (a) Findings\nCongress finds the following:\n**(1)**\nOfficers and employees of the United States Government dutifully and faithfully serve the United States, often placing themselves at serious risk of death or bodily harm, in order to preserve, protect, and defend the interests of the United States.\n**(2)**\nIn prohibiting the assaulting, resisting, or impeding of officers and employees of the United States Government, Congress intended to maximize protection for Federal officers and employees and ensure that individuals who kill or assault Federal officers or employees are prosecuted.\n**(3)**\nThe United States Court of Appeals for the Sixth Circuit analyzed section 111 of title 18, United States Code, correctly when it found, Categorizing \u00a7 111(a)(1) as a general intent crime furthers the congressional objective: If a person acts in a manner which is assaultive toward a Federal official, without specifically intending harm or the apprehension of imminent harm, the official still would be impeded in the performance of his official duties. United States v. Kimes, 246 F.3d 800, 809 (6th Cir. 2001), quoting United States v. Jennings, 855 F. Supp. 1427, 1440 (M.D. Pa. 1994).\n**(4)**\nFederal courts, including the United States Courts of Appeals for the Second, Fourth, Sixth, Seventh, Eighth, Ninth, and Eleventh Circuits, have correctly interpreted section 111 of title 18, United States Code, to be a crime of general intent rather than a crime of specific intent.\n**(5)**\nOther Federal courts, including the United States Courts of Appeals for the First, Fifth, and Tenth Circuits, have issued decisions with language arguably suggesting that section 111 of title 18, United States Code, is a crime of specific intent rather than a crime of general intent, creating the appearance of a split among the United States courts of appeals.\n**(6)**\nIn light of the appearance of a split among the United States courts of appeals described in paragraph (5), it has become necessary for Congress to clarify its original intent that section 111 of title 18, United States Code, is a crime of general intent.\n##### (b) Amendment\nSection 111 of title 18, United States Code, is amended by adding at the end the following:\n(d) Knowledge of defendant In a prosecution for an offense under subsection (a), the Government need not prove that the defendant\u2014 (1) knew that the victim of the offense was a person designated in section 1114 or performed official duties during service as a person so designated; or (2) acted with any intent greater than knowledge. .\n#### 4. Motor vehicles\nSection 2119 of title 18, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1)\u2014\n**(A)**\nby striking , with the intent to cause death or serious bodily harm ;\n**(B)**\nby inserting a comma after force and violence ; and\n**(C)**\nby inserting or conspires after attempts ;\n**(2)**\nin paragraph (1), by striking 15 years and inserting 20 years ;\n**(3)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively;\n**(4)**\nby inserting after paragraph (1) the following:\n(2) if a dangerous weapon or device is used in committing, or in attempting to commit, the offense, be fined under this title or imprisoned not more than 25 years, or both, ; and\n**(5)**\nin paragraph (3), as so redesignated, by striking 25 years and inserting 40 years .\n#### 5. Penalties for firearms offenses\nSection 924(c)(3)(B) of title 18, United States Code, is amended to read as follows:\n(B) is a conspiracy, or an attempt, to commit an offense that has as an element the use, attempted use, or threatened use of physical force against the person or property of another. .\n#### 6. Offenses involving candy-flavored controlled substances manufactured or distributed for minors\n##### (a) In general\nPart D of the Controlled Substances Act ( 21 U.S.C. 841 et seq. ) is amended by inserting after section 418 the following:\n418a. Manufacturing or distributing candy-flavored controlled substances for minors (a) Except as provided in subsection (c) and in section 418, 419, or 420, a person shall be subject to the penalty described in subsection (b) if the person violates section 401(a)(1)\u2014 (1) by manufacturing, creating, distributing, dispensing, or possessing with intent to distribute a controlled substance listed in schedule I or II that is\u2014 (A) combined with a candy or beverage product; (B) marketed or packaged to appear similar to a candy or beverage product; or (C) modified by flavoring or coloring to appear similar to a candy or beverage product; and (2) knowing, or having reasonable cause to believe, that the controlled substance will be distributed, dispensed, or sold to a person under 18 years of age. (b) The penalty described in this subsection is\u2014 (1) in the case of a first offense involving the same controlled substance and schedule, an additional term of imprisonment of not more than 10 years; and (2) in the case of a second or subsequent offense involving the same controlled substance and schedule, an additional term of imprisonment of not more than 20 years. (c) Subsection (a) shall not apply to any controlled substance that\u2014 (1) has been approved by the Secretary under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ), if the contents, marketing, and packaging of the controlled substance have not been altered from the form approved by the Secretary; or (2) has been altered at the direction of a practitioner who is acting for a legitimate medical purpose in the usual course of professional practice. .\n##### (b) Technical and conforming amendment\nThe table of contents for the Comprehensive Drug Abuse Prevention and Control Act of 1970 ( Public Law 91\u2013513 ; 84 Stat. 1236) is amended by inserting after the item relating to section 418 the following:\nSec. 418a. Manufacturing or distributing candy-flavored controlled substances for minors. .\n##### (c) Sentencing Guidelines\nPursuant to its authority under section 994 of title 28, United States Code, and in accordance with this section, the United States Sentencing Commission shall amend and review the Federal sentencing guidelines and policy statements to ensure that the guidelines provide for a penalty enhancement of not less than 2 offense levels for a violation of section 401(a)(1) of the Controlled Substances Act ( 21 U.S.C. 841(a)(1) ) if the defendant\u2014\n**(1)**\nmanufactures, creates, distributes, dispenses, or possesses with intent to distribute a controlled substance listed in schedule I or II that is\u2014\n**(A)**\ncombined with a candy or beverage product;\n**(B)**\nmarketed or packaged to appear similar to a candy or beverage product; or\n**(C)**\nmodified by flavoring or coloring to appear similar to a candy or beverage product; and\n**(2)**\nknows, or has reasonable cause to believe, that the controlled substance will be distributed, dispensed, or sold to a person under 18 years of age.\n#### 7. Kidnapping\nSection 1201 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking subsection (a) and inserting the following:\n(a) Kidnapping (1) Offense Except as provided in paragraph (2), it shall be unlawful for any person, in any circumstance described in paragraph (3), to\u2014 (A) unlawfully\u2014 (i) seize, confine, kidnap, abduct, or carry away an individual by\u2014 (I) force and violence; or (II) intimidation; or (ii) inveigle or decoy an individual; and (B) hold the individual described in subparagraph (A) for ransom, reward, or otherwise. (2) Exception Paragraph (1) shall not apply to an act done against a minor by the parent thereof. (3) Circumstances A circumstance described in this paragraph is that\u2014 (A) the individual is willfully transported in interstate or foreign commerce, regardless of whether the individual was alive when transported across a State boundary, or the offender travels in interstate or foreign commerce or uses the mail or any means, facility, or instrumentality of interstate or foreign commerce in committing or in furtherance of the commission of the offense; (B) any such act against the individual is done within the special maritime and territorial jurisdiction of the United States; (C) any such act against the individual is done within the special aircraft jurisdiction of the United States, as defined in section 46501 of title 49; (D) the individual is a foreign official, an internationally protected person, or an official guest, as those terms are defined in section 1116(b) of this title; or (E) the individual is among those officers and employees described in section 1114 of this title and any such act against the individual is done while the individual is engaged in, or on account of, the performance of official duties. (4) Penalty Any person who commits a violation under this subsection shall be punished by imprisonment for any term of years or for life and, if the death of any individual results, shall be punished by death or life imprisonment. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking subsection (a)(1), above, and inserting subsection (a)(3)(A) ;\n**(B)**\nby striking he and inserting the victim ;\n**(C)**\nby striking such person and inserting such individual ; and\n**(D)**\nby striking under this section and inserting under this subsection ; and\n**(3)**\nin subsection (f), by striking subsection (a)(4) each place it appears and inserting subsection (a) with respect to a circumstance described in paragraph (3)(D) of that subsection .",
      "versionDate": "2025-06-04",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-25T12:46:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-04",
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
          "measure-id": "id119s1949",
          "measure-number": "1949",
          "measure-type": "s",
          "orig-publish-date": "2025-06-04",
          "originChamber": "SENATE",
          "update-date": "2026-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1949v00",
            "update-date": "2026-04-17"
          },
          "action-date": "2025-06-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Combating Violent and Dangerous Crime Act</strong></p><p>This bill expands the definition of <em>crime of violence</em> for the purposes of determining whether a defendant is subject to an enhanced criminal penalty for using or carrying a firearm in the crime of violence. The bill also expands applicable\u00a0criminal penalties for\u00a0bank robbery,\u00a0carjacking, and kidnapping offenses, as well as certain drug offenses.</p><p>Under current law, an individual who uses or carries a firearm in a crime of violence is subject to an enhanced mandatory minimum prison term in addition and consecutive to any other prison term imposed for the underlying crime of violence. The term <em>crime of violence</em> includes a felony that has as an element the use, attempted use, or threatened use of physical force.\u00a0This bill expands <em>crime of violence</em> to include a conspiracy or an attempt to commit a felony that has as an element the use, attempted use, or threatened use of physical force.</p><p>This bill\u00a0expands applicable penalties for federal criminal offenses involving bank robbery, carjacking, or kidnapping, including by specifying the offenses that include as an element force or threat, or intimidation, and therefore qualify as a\u00a0<em>crime of violence</em> under the existing definition.</p><p>Additionally, a conspiracy or attempt to commit a federal bank robbery, carjacking or kidnapping offense qualifies as a <em>crime of violence</em> under the expanded definition.</p><p>Finally, the bill establishes additional criminal penalties for certain federal drug offenses involving the manufacture or distribution of candy-flavored controlled substances or similar products for minors.</p>"
        },
        "title": "Combating Violent and Dangerous Crime Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1949.xml",
    "summary": {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Combating Violent and Dangerous Crime Act</strong></p><p>This bill expands the definition of <em>crime of violence</em> for the purposes of determining whether a defendant is subject to an enhanced criminal penalty for using or carrying a firearm in the crime of violence. The bill also expands applicable\u00a0criminal penalties for\u00a0bank robbery,\u00a0carjacking, and kidnapping offenses, as well as certain drug offenses.</p><p>Under current law, an individual who uses or carries a firearm in a crime of violence is subject to an enhanced mandatory minimum prison term in addition and consecutive to any other prison term imposed for the underlying crime of violence. The term <em>crime of violence</em> includes a felony that has as an element the use, attempted use, or threatened use of physical force.\u00a0This bill expands <em>crime of violence</em> to include a conspiracy or an attempt to commit a felony that has as an element the use, attempted use, or threatened use of physical force.</p><p>This bill\u00a0expands applicable penalties for federal criminal offenses involving bank robbery, carjacking, or kidnapping, including by specifying the offenses that include as an element force or threat, or intimidation, and therefore qualify as a\u00a0<em>crime of violence</em> under the existing definition.</p><p>Additionally, a conspiracy or attempt to commit a federal bank robbery, carjacking or kidnapping offense qualifies as a <em>crime of violence</em> under the expanded definition.</p><p>Finally, the bill establishes additional criminal penalties for certain federal drug offenses involving the manufacture or distribution of candy-flavored controlled substances or similar products for minors.</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s1949"
    },
    "title": "Combating Violent and Dangerous Crime Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Combating Violent and Dangerous Crime Act</strong></p><p>This bill expands the definition of <em>crime of violence</em> for the purposes of determining whether a defendant is subject to an enhanced criminal penalty for using or carrying a firearm in the crime of violence. The bill also expands applicable\u00a0criminal penalties for\u00a0bank robbery,\u00a0carjacking, and kidnapping offenses, as well as certain drug offenses.</p><p>Under current law, an individual who uses or carries a firearm in a crime of violence is subject to an enhanced mandatory minimum prison term in addition and consecutive to any other prison term imposed for the underlying crime of violence. The term <em>crime of violence</em> includes a felony that has as an element the use, attempted use, or threatened use of physical force.\u00a0This bill expands <em>crime of violence</em> to include a conspiracy or an attempt to commit a felony that has as an element the use, attempted use, or threatened use of physical force.</p><p>This bill\u00a0expands applicable penalties for federal criminal offenses involving bank robbery, carjacking, or kidnapping, including by specifying the offenses that include as an element force or threat, or intimidation, and therefore qualify as a\u00a0<em>crime of violence</em> under the existing definition.</p><p>Additionally, a conspiracy or attempt to commit a federal bank robbery, carjacking or kidnapping offense qualifies as a <em>crime of violence</em> under the expanded definition.</p><p>Finally, the bill establishes additional criminal penalties for certain federal drug offenses involving the manufacture or distribution of candy-flavored controlled substances or similar products for minors.</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s1949"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1949is.xml"
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
      "title": "Combating Violent and Dangerous Crime Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Combating Violent and Dangerous Crime Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve certain criminal provisions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T05:33:16Z"
    }
  ]
}
```
