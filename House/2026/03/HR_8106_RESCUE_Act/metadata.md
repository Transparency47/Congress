# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8106
- Title: RESCUE Act
- Congress: 119
- Bill type: HR
- Bill number: 8106
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-05-11T20:20:07Z
- Update date including text: 2026-05-11T20:20:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8106",
    "number": "8106",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000398",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
        "lastName": "Kean",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "RESCUE Act",
    "type": "HR",
    "updateDate": "2026-05-11T20:20:07Z",
    "updateDateIncludingText": "2026-05-11T20:20:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-03-26T14:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-26T14:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8106ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8106\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Kean introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo impose sanctions with respect to Rosatom, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rosatom Energy Sanctions Compliance and Unified Enforcement Act or the RESCUE Act .\n#### 2. Statement of policy\nIt shall be the policy of the United States\u2014\n**(1)**\nto end United States reliance on the nuclear energy sector of the Russian Federation, including State Atomic Energy Corporation Rosatom (Rosatom), in light of Russia\u2019s unprovoked war of aggression against Ukraine, a grave breach of international law;\n**(2)**\nto work with United States allies and partners to find alternative nuclear energy suppliers to Russia and help these allies and partners end their reliance on Rosatom;\n**(3)**\nto limit access of the Government of Russia to revenue through the implementation of sanctions and export controls against Rosatom; and\n**(4)**\nto inhibit the Government of Russia from using Rosatom as a tool of malign influence internationally.\n#### 3. Strategy\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 4 years, the President shall submit to the appropriate congressional committees a strategy that contains the contents described in subsection (b).\n##### (b) Contents described\nThe contents of the strategy required by subsection (a) shall include the following:\n**(1)**\nA strategy to\u2014\n**(A)**\nwork with United States allies and partners to find alternative nuclear energy suppliers to Russia and help these allies and partners end their reliance on Rosatom;\n**(B)**\neffect a permanent decoupling of the United States from the Russian nuclear energy industry; and\n**(C)**\nreplace Rosatom as the primary entity that can provide reactor safety, operation, and overhaul services to the existing Rosatom and Russian Federation designed and constructed nuclear reactor fleet.\n**(2)**\nA description of key vulnerabilities in the infrastructure and nuclear energy supply chains of United States allies and partners that are related to Rosatom or its subsidiaries.\n**(3)**\nA description of consultations carried out with United States allies and partners in implementing the sanctions required by sections 4 and 5.\n**(4)**\nA description of proposed assistance by the United States and United States allies and partners to the International Atomic Energy Agency\u2019s international low-enriched uranium fuel bank in Kazakhstan.\n**(5)**\nA description of feasible efforts the United States can take to ensure that foreign persons, including foreign financial institutions, sanctioned pursuant to this Act are not able to evade such sanctions by routing nuclear materials from Russia through third-party vendors or entrepots.\n##### (c) Form\nThe strategy required by subsection (a) shall be submitted in unclassified form, but may contain a classified annex.\n#### 4. Imposition of sanctions with respect to rosatom\n##### (a) Sanctions required\nOn and after the date that is 180 days after the date of the enactment of this Act, the President shall impose the sanction described in subsection (b) with respect to\u2014\n**(1)**\nany foreign person that the President determines\u2014\n**(A)**\noperates in the nuclear energy sector of the Russian Federation; and\n**(B)**\nis owned or controlled by the Government of the Russian Federation;\n**(2)**\nany foreign person that the President determines knowingly engages, after the date of enactment of this Act, in\u2014\n**(A)**\nthe approval or entering into of any contract for the construction of any new nuclear reactor intended to be constructed, operated, serviced, or maintained by a foreign entity described under paragraph (1);\n**(B)**\nany significant transaction for or related to construction in connection with any new nuclear reactor intended to be constructed, operated, serviced, or maintained by a foreign entity described in paragraph (1); or\n**(C)**\nthe provision of construction-related services in connection with any new nuclear reactor intended to be constructed, operated, serviced, or maintained by a foreign entity described in paragraph (1); and\n**(3)**\nany foreign person that is owned, controlled, or directed by any foreign person described in paragraph (1) or (2).\n##### (b) Sanctions described\nThe President shall exercise all of the powers granted by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to block and prohibit all transactions in all property and interests in property of the foreign person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n##### (c) Prohibitions and conditions with respect to certain accounts held by foreign financial institutions\n**(1) In general**\nThe President may prescribe regulations to prohibit, or impose strict conditions on, the opening or maintaining in the United States of a correspondent account or a payable-through account by a foreign financial institution that the President determines has, after the date of enactment of this act, facilitated the activities of a foreign person described in section 4(a).\n**(2) Definitions**\nIn this subsection:\n**(A) Correspondent account; payable-through account**\nThe terms correspondent account , and payable-through account have the meanings given those terms in section 5318A of title 31, United States Code.\n**(B) Foreign financial institution**\nThe term foreign financial institution has the meaning given that term under section 1010.605 of title 31, Code of Federal Regulations.\n##### (d) Termination of primary sanctions\nThe President may terminate the sanctions required under subsection (a) with respect to foreign persons described in paragraph (1) of such subsection if, not later than 30 days before the termination of such sanctions, the President certifies in writing to the appropriate congressional committees that\u2014\n**(1)**\nthe Russian Federation has ceased hostilities in Ukraine, has withdrawn all of its forces from Ukraine\u2019s internationally recognized territory, and Ukraine\u2019s territorial integrity is fully restored to its internationally recognized borders as of January 1, 2014;\n**(2)**\nRosatom is not contributing to the misuse of United States-origin nuclear material within Zaporizhzhia Nuclear Power Plant;\n**(3)**\nRussia, through Rosatom, is not using or gaining any benefit of the proceeds from sales related to Rosatom to fund Russia\u2019s illegal occupation of Ukraine or other territory;\n**(4)**\nRussia is in full compliance with the Treaty between the United States of America and the Russian Federation on Measures for the Further Reduction and Limitation of Strategic Offensive Arms until such time that the treaty remains in effect or until a new treaty is negotiated and comes into force; and\n**(5)**\nRosatom\u2019s transfer of nuclear materials and assistance to third-party countries does not contribute to any such country\u2019s nuclear weapons activity or illicit nuclear activity.\n##### (e) Exception with respect to verifiable steps To change conduct\nThe President shall not be required to impose sanctions under subsection (a) with regards to a foreign person described under paragraph (2) or (3) of that subsection if the President certifies in writing to the appropriate congressional committees that\u2014\n**(1)**\nthe foreign person\u2014\n**(A)**\nno longer meets the description of a foreign person described in paragraph (2) or (3) of section 4(a); or\n**(B)**\nhas taken and is continuing to take significant, verifiable steps toward no longer meeting the description of a foreign person described in paragraph (2) or (3) of section 4(a); and\n**(2)**\nthe foreign person has provided reliable assurances that the foreign person will not reinitiate described by paragraphs (2) or (3) of section 4(a), or will continue to make progress toward terminating such activities, as the case may be.\n##### (f) Waivers\n**(1) In general**\nThe President may waive the application of sanctions under subsection (a) on a case-by-case basis for renewable periods of 180 days if the President certifies to the appropriate congressional committees, not later than 15 days before the entry into effect of such waiver, that the waiver is in the national security interest of the United States.\n**(2) Transactions relating to activities necessary to the production of medical isotopes and industrial isotopes**\n**(A) In general**\nThe President may waive the application of sanctions under subsection (a) for a transaction or transactions for periods not to exceed one year, renewable for up to 7 years, if\u2014\n**(i)**\nthe President determines that the transaction or transactions relate to activities necessary to the production of medical isotopes or industrial isotopes; and\n**(ii)**\nthe President certifies to the appropriate congressional committees that\u2014\n**(I)**\ndomestic medical isotope or industrial isotope production is insufficient to meet United States patient and industry requirements; and\n**(II)**\nthe United States is taking measurable steps to establish medical isotope or industrial isotope supply chains that are not reliant on Rosatom or other Russian source material.\n**(B) Definitions**\nIn this paragraph:\n**(i) Industrial isotope**\nThe term industrial isotope means a radioactive or stable form of an element that is used primarily for industrial (non-medical) purposes.\n**(ii) Medical isotope**\nThe term medical isotope means a radioactive or stable form of an element that is either administered directly into a patient, is combined with a carrier molecule for diagnosis and treatment of disease, is contained within a medical device for diagnosis and treatment of disease, is used in the production of these isotopes, or is used primarily to sterilize medical devices or pharmaceutical products.\n##### (g) Exceptions\n**(1)**\nSanctions under this section shall not apply to\u2014\n**(A)**\nany activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. );\n**(B)**\nany authorized intelligence activities of the United States;\n**(C)**\nactivities that are for the conduct of the official business of the United Nations, its specialized agencies, programmes, funds, and related organizations by employees, contractors, or grantees of such agencies, programmes and funds; or\n**(D)**\nany activities that are required for the safe operation of nuclear reactors, including critical reactor safety, safeguards, and security, in which there are no alternative suppliers.\n**(2) Exception relating to importation of goods**\nA requirement to block and prohibit all transactions in all property and interests in property pursuant to sanctions under this section shall not include the authority or a requirement to impose sanctions on the importation of goods.\n**(3) Exception to comply with the united nations headquarters agreement and law enforcement activities**\nSanctions under this section shall not apply with respect to the admission of an alien to the United States if admitting or paroling the alien into the United States is necessary\u2014\n**(A)**\nto permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations of the United States; or\n**(B)**\nto carry out or assist authorized law enforcement activity in the United States.\n**(4) Humanitarian assistance**\nSanctions under this section shall not apply with respect to\u2014\n**(A)**\nthe conduct or facilitation of a transaction for the provision of agricultural commodities, food, medicine, medical devices, or humanitarian assistance, or for humanitarian purposes; or\n**(B)**\ntransactions that are necessary for, or related to, the activities described in subparagraph (A).\n**(5) Definitions**\nIn this subsection:\n**(A) Agricultural commodity**\nThe term agricultural commodity has the meaning given such term in section 102 of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5602 ).\n**(B) Good**\nThe term good means any article, natural or manmade substance, material, supply, or manufactured product, including inspection and test equipment, and excluding technical data.\n**(C) Medical device**\nThe term medical device has the meaning given the term device in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(D) Medicine**\nThe term medicine has the meaning given the term drug in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n##### (h) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to a person that violates, attempts to violate, conspires to violate, or causes a violation of regulations promulgated under subsection (d) to carry out this section to the same extent that such penalties apply to a person that commits an unlawful act described in section 206(a) of that Act.\n##### (i) Regulatory authority\nNot later than 180 days after the date of the enactment of this Act, the President shall promulgate regulations as necessary for the implementation of this section.\n##### (j) Sunset\nThe authority to impose sanctions under this section shall terminate on the date that is 7 years after the date of enactment of this Act.\n#### 5. Congressional oversight of certain sanctions imposed with respect to the Russian Federation\n##### (a) In general\nNot later than 30 days after receiving a request from the chairman and ranking member of one of the appropriate congressional committees with respect to whether a person meets the criteria of a foreign person described in section 4(a) or is violating or has violated a covered regulation, the President shall\u2014\n**(1)**\ndetermine if the person meets such criteria; and\n**(2)**\nsubmit a classified or unclassified report to such chairman and ranking member with respect to such determination that includes a statement of whether the President imposed or intends to impose sanctions with respect to such person.\n##### (b) Covered regulation defined\nThe term covered regulation means the following regulations as they are in effect on the date of enactment of this Act\u2014\n**(1)**\npart 587 of title 31, Code of Federal Regulations (Russia Harmful Foreign Activities Sanctions Regulations); or\n**(2)**\npart 589 of title 31, Code of Federal Regulations (Ukraine/Russia-Related Sanctions Regulations).\n#### 6. Statement of policy regarding the Russia 123 agreement and required report\n##### (a) Statement of policy\nIt is the policy of the United States that any agreement entered into pursuant to section 123 of the Atomic Energy Act of 1954 ( 42 U.S.C. 2153 ) should be in the national security interest of the United States and advance non-proliferation principles and the safe operation of nuclear reactors.\n##### (b) Report required\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees a report on the Agreement between the Government of the United States of America and the Government of the Russian Federation for Cooperation in the Field of Peaceful Uses of Nuclear Energy, entered into on January 11, 2011, pursuant to section 123 of the Atomic Energy Act of 1954 ( 42 U.S.C. 2153 ), as well as the manner and extent to which remaining in the agreement is beneficial to the United States national security interest and non-proliferation objectives.\n##### (c) Contents of report\nThe report required by subsection (b) shall include assessments and detailed descriptions of\u2014\n**(1)**\nthe extent to which Rosatom, its subsidiaries or any agent of the Russian Federation is contributing or has contributed to the misuse of United States-origin or deemed nuclear material within Zaporizhzhia Nuclear Power Plant;\n**(2)**\nthe extent to which Russia, through Rosatom and its subsidiaries, is using or gaining any benefit of the proceeds from sales or in-kind transfers related to Rosatom to fund Russia\u2019s illegal occupation of Ukraine or other territory;\n**(3)**\nthe extent to which Russia has conducted any yield-producing nuclear test in the 10-year period ending on the date of the certification;\n**(4)**\nthe extent to which Rosatom\u2019s transfer of nuclear materials and assistance to third countries contributes to any such third-party country\u2019s nuclear weapons activity or illicit nuclear activity;\n**(5)**\nthe extent to which Russia is transferring nuclear material or nuclear weapons development with a country or countries in which the International Atomic Energy Agency has an open investigation or has withdrawn from the Treaty on the Non-Proliferation of Nuclear Weapons;\n**(6)**\nthe extent to which Russia has met its obligations under the Plutonium Management and Disposition Agreement;\n**(7)**\nthe extent to which Rosatom, its subsidiaries, or any agent of the Russian federation is contributing to the People\u2019s Republic of China\u2019s destabilizing and dangerous nuclear weapons expansion;\n**(8)**\nthe extent to which Rosatom or its subsidiaries is using funds received from commercial transactions to support, both financially or materially, their contribution to the nuclear weapons program of the Russian Federation; and\n**(9)**\nthe role the Agreement between the Government of the United States of America and the Government of the Russian Federation for Cooperation in the Field of Peaceful Uses of Nuclear Energy, entered into on January 11, 2011, pursuant to section 123 of the Atomic Energy Act of 1954 ( 42 U.S.C. 2153 ) plays in advancing United States national security and non-proliferation objectives and any expected positive and negative impacts were the United States to withdraw from such agreement.\n#### 7. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs and the Committee on Financial Services of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(2) Foreign person**\nThe term foreign person means\u2014\n**(A)**\nan individual who is not a United States citizen or an alien lawfully admitted for permanent residence to the United States; or\n**(B)**\nan entity that is not a United States person.\n**(3) United States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or of any jurisdiction of the United States, including a foreign branch of such an entity; or\n**(C)**\na person in the United States.\n**(4) Rosatom**\nThe term Rosatom means the State Atomic Energy Corporation Rosatom or any successor entity.",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in House"
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
        "name": "International Affairs",
        "updateDate": "2026-05-11T20:20:07Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8106ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "RESCUE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T04:53:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESCUE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rosatom Energy Sanctions Compliance and Unified Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To impose sanctions with respect to Rosatom, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:49:01Z"
    }
  ]
}
```
