# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/363?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/363
- Title: STOP MADNESS Act
- Congress: 119
- Bill type: S
- Bill number: 363
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2025-06-11T16:46:45Z
- Update date including text: 2025-06-11T16:46:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/363",
    "number": "363",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "STOP MADNESS Act",
    "type": "S",
    "updateDate": "2025-06-11T16:46:45Z",
    "updateDateIncludingText": "2025-06-11T16:46:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
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
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T22:25:32Z",
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
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "OH"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "IN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NE"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "MT"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s363is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 363\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mr. Scott of South Carolina (for himself and Mr. Moreno ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo impose sanctions with respect to foreign governments that resist efforts to repatriate their citizens who have unlawfully entered the United States and foreign governments and foreign persons that knowingly facilitate unlawful immigration into the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stifling Transnational Operations and Proliferators by Mitigating Activities that Drive Narcotics, Exploitation, and Smuggling Sanctions Act or the STOP MADNESS Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nmigrants who have unlawfully entered the United States\u2014\n**(A)**\nare a threat to national security; and\n**(B)**\nshould be repatriated to their countries of origin;\n**(2)**\nif a country of origin resists repatriation of its citizens that unlawfully entered the United States, that country should be subject to economic sanctions, denying the country access to the United States financial system; and\n**(3)**\nany country, entity, or individual that knowingly facilitates unlawful immigration into the United States should be subject to economic sanctions, denying them access to the United States financial system.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs and the Committee on Financial Services of the House of Representatives.\n**(2) Foreign government**\nThe term foreign government \u2014\n**(A)**\nmeans any governing body or political organization that exercises control over a foreign country or a substantial portion of a foreign country; and\n**(B)**\nincludes\u2014\n**(i)**\na ministry, department, agency, or instrumentality of a body or organization described in subparagraph (A);\n**(ii)**\nan official, representative, or other individual acting on behalf of such a body or organization, including an individual who holds a formal or informal role of authority; and\n**(iii)**\nan entity\u2014\n**(I)**\nowned or controlled by such a body or organization; or\n**(II)**\nthat acts on behalf of or is directed by such a body or organization.\n**(3) Foreign person**\nThe term foreign person \u2014\n**(A)**\nmeans an individual or entity that is not a United States person; and\n**(B)**\ndoes not include a foreign government.\n**(4) Knowingly**\nThe term knowingly , with respect to conduct, a circumstance, or a result, means that a person has actual knowledge, or should have known, of the conduct, the circumstance, or the result.\n**(5) United States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen;\n**(B)**\nan alien lawfully admitted for permanent residence to the United States;\n**(C)**\nan alien lawfully admitted to the United States, including any alien admitted for temporary residence, tourism, or employment, or to pursue a course of study; or\n**(D)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity.\n#### 4. Sense of Congress; statement of policy\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nforeign governments that refuse or obstruct the efforts of the United States to repatriate their citizens who have unlawfully entered the United States constitute an unusual and extraordinary threat to the national security, foreign policy, and economy of the United States, and pose a national emergency; and\n**(2)**\nforeign governments and foreign persons that knowingly facilitate unlawful immigration into the United States constitute an unusual and extraordinary threat to the national security, foreign policy, and economy of the United States, and pose a national emergency.\n##### (b) Statement of policy\nIt is the policy of the United States, in order to protect the national security of the United States, to apply economic and other financial sanctions with respect to\u2014\n**(1)**\nforeign governments that resist efforts to repatriate their citizens who have unlawfully entered the United States; and\n**(2)**\nforeign governments and foreign persons that knowingly facilitate unlawful immigration into the United States.\n#### 5. Use of national emergency authorities; reporting\n##### (a) In general\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this Act.\n##### (b) Report required\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter until the date that is 7 years after such date of enactment, the President shall submit to the appropriate congressional committees a report on actions taken by the executive branch pursuant to this Act and any national emergency declared with respect to the facilitation of unlawful immigration to the United States, including\u2014\n**(A)**\nthe issuance of any new or revised regulations, policies, or guidance;\n**(B)**\nthe imposition of sanctions;\n**(C)**\nthe collection of relevant information from outside parties;\n**(D)**\nthe issuance or termination of general licenses, specific licenses, and statements of licensing policy by the Office of Foreign Assets Control of the Department of the Treasury;\n**(E)**\nany pending enforcement actions; or\n**(F)**\nthe implementation of mitigation procedures.\n**(2) Form of report**\nEach report required by paragraph (1) shall be submitted in unclassified form, but may include the matters required by subparagraphs (C), (D), (E), and (F) of that paragraph in a classified annex.\n#### 6. Imposition of sanctions with respect to efforts to resist repatriation or facilitate unlawful immigration\n##### (a) In general\nThe President may impose the sanctions described in subsection (b) with respect to\u2014\n**(1)**\nany foreign government the President determines knowingly refuses or obstructs the efforts of the United States to repatriate its citizens who have unlawfully entered the United States; and\n**(2)**\nany foreign government or foreign person the President determines knowingly facilitates unlawful immigration into the United States.\n##### (b) Sanctions described\nThe President may, pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ), block and prohibit all transactions in property and interests in property of a foreign government or foreign person described in subsection (a) if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n##### (c) Report required\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter until the date that is 7 years after such date of enactment, the President shall submit to the appropriate congressional committees a report on actions taken by the executive branch with respect to the foreign governments and foreign persons identified under subsection (a).\n#### 7. Penalties; waivers; exceptions\n##### (a) Penalties\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this Act or any regulation, license, or order issued to carry out this Act shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (b) National security waiver\nThe President may waive the application of sanctions under this Act with respect to a foreign government or foreign person if the President determines that the waiver is in the national security interest of the United States.\n##### (c) Exceptions for intelligence and law enforcement activities\nThis Act shall not apply with respect to\u2014\n**(1)**\nactivities subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence activities of the United States; or\n**(2)**\nactivities necessary to carry out or assist law enforcement activity of the United States.",
      "versionDate": "2025-02-03",
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
        "name": "Immigration",
        "updateDate": "2025-03-07T14:32:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-03",
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
          "measure-id": "id119s363",
          "measure-number": "363",
          "measure-type": "s",
          "orig-publish-date": "2025-02-03",
          "originChamber": "SENATE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s363v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-02-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stifling Transnational Operations and Proliferators by Mitigating Activities that Drive Narcotics, Exploitation, and Smuggling Sanctions Act or the STOP MADNESS Act</strong></p><p>This bill allows the President to impose sanctions on (1) foreign governments the President determines knowingly refuse or obstruct U.S. efforts to repatriate its citizens who have unlawfully entered the United States, and (2) foreign governments or foreign persons the President determines knowingly facilitate unlawful immigration into the United States.</p><p>The President may waive sanctions if the President determines that it is in the national security interest of the United States.</p><p>If a person violates this bill, criminal and civil penalties applicable to violations of the International Emergency Economic Powers Act (IEEPA) apply.</p><p>To carry out the bill, the President may exercise authorities under the\u00a0IEEPA.</p>"
        },
        "title": "STOP MADNESS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s363.xml",
    "summary": {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stifling Transnational Operations and Proliferators by Mitigating Activities that Drive Narcotics, Exploitation, and Smuggling Sanctions Act or the STOP MADNESS Act</strong></p><p>This bill allows the President to impose sanctions on (1) foreign governments the President determines knowingly refuse or obstruct U.S. efforts to repatriate its citizens who have unlawfully entered the United States, and (2) foreign governments or foreign persons the President determines knowingly facilitate unlawful immigration into the United States.</p><p>The President may waive sanctions if the President determines that it is in the national security interest of the United States.</p><p>If a person violates this bill, criminal and civil penalties applicable to violations of the International Emergency Economic Powers Act (IEEPA) apply.</p><p>To carry out the bill, the President may exercise authorities under the\u00a0IEEPA.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s363"
    },
    "title": "STOP MADNESS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stifling Transnational Operations and Proliferators by Mitigating Activities that Drive Narcotics, Exploitation, and Smuggling Sanctions Act or the STOP MADNESS Act</strong></p><p>This bill allows the President to impose sanctions on (1) foreign governments the President determines knowingly refuse or obstruct U.S. efforts to repatriate its citizens who have unlawfully entered the United States, and (2) foreign governments or foreign persons the President determines knowingly facilitate unlawful immigration into the United States.</p><p>The President may waive sanctions if the President determines that it is in the national security interest of the United States.</p><p>If a person violates this bill, criminal and civil penalties applicable to violations of the International Emergency Economic Powers Act (IEEPA) apply.</p><p>To carry out the bill, the President may exercise authorities under the\u00a0IEEPA.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s363"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s363is.xml"
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
      "title": "STOP MADNESS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STOP MADNESS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stifling Transnational Operations and Proliferators by Mitigating Activities that Drive Narcotics, Exploitation, and Smuggling Sanctions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose sanctions with respect to foreign governments that resist efforts to repatriate their citizens who have unlawfully entered the United States and foreign governments and foreign persons that knowingly facilitate unlawful immigration into the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:31Z"
    }
  ]
}
```
