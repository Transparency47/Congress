# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3519?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3519
- Title: Remote Access Security Act
- Congress: 119
- Bill type: S
- Bill number: 3519
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-13T17:28:34Z
- Update date including text: 2026-01-13T17:28:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3519",
    "number": "3519",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Remote Access Security Act",
    "type": "S",
    "updateDate": "2026-01-13T17:28:34Z",
    "updateDateIncludingText": "2026-01-13T17:28:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T17:58:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "AR"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3519is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3519\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. McCormick (for himself, Mr. Wyden , Mr. Cotton , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 to provide for control of remote access to items, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Remote Access Security Act .\n#### 2. Control of remote access of items under the Export Control Reform Act of 2018\n##### (a) Definition of remote access\nSection 1742 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 ) is amended by adding at the end the following:\n(15) Remote access (A) In general The term remote access means access to an item subject to the jurisdiction of the United States and included on the Commerce Control List set forth in Supplement No. 1 to part 774 of the Export Administration Regulations, by a foreign person of concern through a cloud infrastructure service from a location outside the United States and other than where the item is physically located, if the Secretary determines that the use of the item has demonstrated a serious risk to the national security or foreign policy of the United States through the use of software, such as by\u2014 (i) training an artificial intelligence dual-use model that\u2014 (I) substantially lowers the barrier of entry for experts or nonexperts to design, synthesize, acquire, or use chemical, biological, radiological, or nuclear weapons or other weapons of mass destruction; (II) conducts offensive cyber operations through automated vulnerability discovery and exploitation against a wide range of potential targets of cyber attacks (not including for defensive purposes such vulnerability reporting or mitigation); or (III) evades human control or oversight of automated systems through means of deception or obfuscation; (ii) accessing capabilities primarily designed for offensive cyberspace operations (not including accessing such capabilities for network defense activities); or (iii) conducting surveillance primarily designed to undermine human rights, such as by using spyware (as defined in section 1102A of the National Security Act of 1947 ( 50 U.S.C. 3232a(a) )), location tracking technology, or biometric identification technology primarily designed for such surveillance. (B) Cloud infrastructure service defined For purposes of subparagraph (A), the term cloud infrastructure service has the meaning given the term Infrastructure as a Service by the National Institute of Standards and Technology in Special Publication 800\u2013145 (or any successor publication). (16) Foreign person of concern The term foreign person of concern means\u2014 (A) the government of\u2014 (i) a country specified in section 4872(f)(2) of title 10, United States Code; or (ii) any region within such a country, including the Macau Special Administrative Region and the Hong Kong Special Administrative Region of the People\u2019s Republic of China; (B) an entity located or headquartered in, or the ultimate parent company of which is headquartered in, such a country or region; or (C) a person subject to the jurisdiction of a government described in subparagraph (A). .\n##### (b) Statement of policy\nSection 1752 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), by inserting , and provision of remote access to, after export of ; and\n**(B)**\nin subparagraph (B), by inserting , and provision of remote access to, after export of ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by inserting , and provision of remote access to, after transfer of ; and\n**(B)**\nin subparagraph (A), in the matter preceding clause (i), by inserting , or provision of remote access to, after release of .\n##### (c) Authority of President\nSection 1753 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4812 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking and at the end;\n**(B)**\nin paragraph (2)(F), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(3) the provision of remote access to items subject to the jurisdiction of the United States to foreign persons of concern. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (6), by striking and at the end;\n**(B)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(8) regulate the provision of remote access to items described in subsection (a)(3). ; and\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby inserting , or provision of remote access to, after in-country transfer of ;\n**(B)**\nby striking subsections (b)(1) or (b)(2) and inserting paragraphs (1), (2), and (8) of subsection (b), as applicable, ; and\n**(C)**\nby striking or in-country transfer occurs and inserting in-country transfer, or provision of remote access occurs .\n##### (d) Additional authorities\nSection 1754 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by inserting , and provision of remote access to, after transfers of ;\n**(B)**\nin paragraph (4), by inserting , and provision of remote access to, after transfers of ;\n**(C)**\nin paragraph (5), in the matter preceding subparagraph (A), by inserting , and provision of remote access to, after transfers of ;\n**(D)**\nin paragraph (6), by striking United States export control and inserting United States control ;\n**(E)**\nin paragraph (7), by striking export controls and inserting controls ;\n**(F)**\nin paragraph (10), by striking or in-country transferred and inserting in-country transferred, or accessed remotely ;\n**(G)**\nin paragraph (11), by adding at the end before the semicolon the following: or remote access ; and\n**(H)**\nin paragraph (15), by striking to export and inserting for export, reexport, in-country transfer, or provision of remote access ;\n**(2)**\nin subsection (b), by inserting , or provision of remote access to, after transfer of ; and\n**(3)**\nin subsection (d)(1)(A), by inserting , or provision of remote access to, after in country-transfer of .\n##### (e) Administration of controls\nSection 1755 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4814 ) is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (C), by inserting , and provision of remote access to, after in-country transfers of ; and\n**(B)**\nin subparagraph (E), by inserting , and remote access to, after in-country transfers of ; and\n**(2)**\nin subsection (c), by striking export controls and inserting controls .\n##### (f) Licensing\nSection 1756 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4815 ) is amended\u2014\n**(1)**\nin subsection (a), in the matter preceding paragraph (1), by inserting , and provision of remote access to, after in-country transfer of ; and\n**(2)**\nin subsection (b), by inserting , or provide remote access to, after in-country transfer .\n##### (g) Compliance assistance\nSection 1757 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4816 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting , or provision of remote access to, after in-country transfer of ; and\n**(2)**\nin subsection (c)(2), by striking export controls and inserting controls .\n##### (h) Penalties\nSection 1760 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4819 ) is amended\u2014\n**(1)**\nin subsection (a)(2)(F)\u2014\n**(A)**\nin clause (ii), by striking any export control document or any report and inserting any document or report ; and\n**(B)**\nin clause (iii), by inserting , or provision of remote access to, after in-country transfer of ;\n**(2)**\nin subsection (c)(1)(C), by striking or in-country transfer and inserting in-country transfer, or remotely access ; and\n**(3)**\nin subsection (e)(1)(A)\u2014\n**(A)**\nin clause (i), by inserting , or remotely access or provide remote access to, after United States ; and\n**(B)**\nin clause (ii), by striking or in-country transfer and inserting in-country transfer, or remotely access, or provide remote access to, .\n##### (i) Enforcement\nSection 1761 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4820 ) is amended\u2014\n**(1)**\nin subsection (a)(5), by striking or in-country transferred and inserting in-country transferred, or remotely accessed ; and\n**(2)**\nin subsection (h)(1)(B), by inserting , or provide remote access to, after in-country transfer .\n##### (j) Annual report\nSection 1765(a)(1) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4824(a)(1) ) is amended by inserting , and provision of remote access to, after in-country transfers of .\n##### (k) Effect on other Acts\nSection 1767 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4825 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting , or remote access to, after reexport of ; and\n**(2)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A), by inserting , and remote access by and provision of remote access to such persons to, after persons of ; and\n**(B)**\nin subparagraph (C), by striking or in-country transferred and inserting in-country transferred, or remotely accessed .\n##### (l) Termination\nThe authority under part I of the Export Control Reform Act of 2018, as amended by this section, to impose controls on remote access to items terminates on the date that is 10 years after the date of the enactment of this Act.\n#### 3. Consultations with Congress\nThe Secretary of Commerce shall ensure Congress is kept fully and currently informed of any anticipated promulgation of regulations to control remote access to items under the Export Control Reform Act of 2018, as amended by section 2, including ensuring that Congress is informed, in a classified setting as necessary, on\u2014\n**(1)**\nthe national security or foreign policy risk that would be addressed by the regulations;\n**(2)**\nhow the method of the regulations addresses that risk; and\n**(3)**\nhow the regulations may impact the economy of the United States, including the impact on the competitiveness of United States industry in cloud services and related industries as a result of the regulations.\n#### 4. Report and recommendations\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Commerce shall submit to Congress and make available to the public a report assessing and making recommendations with respect to\u2014\n**(1)**\nthe implementation of this Act and the amendments made by this Act;\n**(2)**\nmaximizing the level of privacy, and minimizing compliance costs, for entities seeking licenses relating to remote access to items under the Export Control Reform Act of 2018, as amended by section 2;\n**(3)**\nimproving the speed at which and consistency with which applications for such licenses are reviewed;\n**(4)**\nidentifying relevant national security and foreign policy concerns related to remote access to items in the interest of improving certainty for United States businesses;\n**(5)**\nincreasing cooperation with international partners with respect to remote access to items;\n**(6)**\nensuring export controls relating to remote access to items are consistent, clear, and up to date; and\n**(7)**\nrecommending amendments to the Export Control Reform Act of 2018 to strengthen the provisions of that Act relating to remote access.\n##### (b) Consultations\nIn developing the report required by subsection (a), the Secretary shall seek input from the public, including holding a public roundtable with industry participants.",
      "versionDate": "2025-12-17",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-01-13T17:28:34Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3519is.xml"
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
      "title": "Remote Access Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Remote Access Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Export Control Reform Act of 2018 to provide for control of remote access to items, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T05:33:20Z"
    }
  ]
}
```
