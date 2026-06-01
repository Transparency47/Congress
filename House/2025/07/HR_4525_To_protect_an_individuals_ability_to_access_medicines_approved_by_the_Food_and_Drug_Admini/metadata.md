# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4525?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4525
- Title: Right to FDA-Approved Medicines Act
- Congress: 119
- Bill type: HR
- Bill number: 4525
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-05-01T08:08:08Z
- Update date including text: 2026-05-01T08:08:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4525",
    "number": "4525",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000305",
        "district": "2",
        "firstName": "Deborah",
        "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
        "lastName": "Ross",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Right to FDA-Approved Medicines Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:08Z",
    "updateDateIncludingText": "2026-05-01T08:08:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "WA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NJ"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "GA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TN"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "VA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "WA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "NY"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "WA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "MD"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "OH"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NV"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "TX"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CT"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MD"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4525ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4525\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Ross (for herself, Ms. Schrier , Ms. Castor of Florida , Mrs. Trahan , and Mrs. Fletcher ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo protect an individuals ability to access medicines approved by the Food and Drug Administration to protect a health care providers ability to provide such medicines, and information related to such medicines.\n#### 1. Short title\nThis Act may be cited as the Right to FDA-Approved Medicines Act .\n#### 2. Definitions\nIn this Act:\n**(1) FDA-approved medicine**\nThe term FDA-approved medicine means any drug approved under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or licensed under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ).\n**(2) Government**\nThe term government includes each branch, department, agency, instrumentality, and official of the United States or a State.\n**(3) Health care provider**\nThe term health care provider means any entity or individual (including any physician, certified nurse-midwife, nurse, nurse practitioner, physician assistant, and pharmacist) that is licensed or otherwise authorized by a State to prescribe FDA-approved medicines.\n**(4) State**\nThe term State includes each of the 50 States, the District of Columbia, the Commonwealth of Puerto Rico, and each territory and possession of the United States, and any political subdivision of any of the foregoing, including any unit of local government, such as a county, city, town, village, or other general purpose political subdivision of a State.\n#### 3. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto provide a clear and comprehensive right to FDA-approved medicines; and\n**(2)**\nto permit individuals to seek and obtain FDA-approved medicines and to permit health care providers to facilitate prescribing such medicines.\n#### 4. Permitted services\n##### (a) In general\nAn individual has a statutory right under this Act to obtain FDA-approved medicines free from coercion, and a health care provider has a corresponding right to provide FDA-approved medicines, and information, referrals, and services related to such medicines.\n##### (b) Limitations or requirements\nThe statutory rights specified in subsection (a) shall not be limited or otherwise infringed through any limitation or requirement that\u2014\n**(1)**\nexpressly, effectively, implicitly, or as-implemented singles out\u2014\n**(A)**\nthe provision of FDA-approved medicines, or information related to such medicines;\n**(B)**\nhealth care providers who provide FDA-approved medicines or information related to such medicines; or\n**(C)**\nfacilities in which FDA-approved medicines or information related to such medicines; and\n**(2)**\nimpedes access to FDA-approved medicines or information related to such medicines.\n##### (c) Exception\nTo defend against a claim that a limitation or requirement violates a health care provider\u2019s or individual\u2019s statutory rights under subsection (b), a party must establish, by clear and convincing evidence, that\u2014\n**(1)**\nthe limitation or requirement significantly advances access to FDA-approved medicines, and information related to such medicines; and\n**(2)**\naccess to FDA-approved medicines and information related to such medicines or the health of patients cannot be advanced by a less restrictive alternative measure or action.\n##### (d) Rule of construction\nNothing in this section shall be construed to limit the authority of the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to approve a drug under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or license a drug under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ), or for the Federal Government to enforce such approval or licensure.\n#### 5. Applicability and preemption\n##### (a) General application\n**(1) In general**\nExcept as provided in subsection (c), this Act supersedes and applies to the law of the Federal Government and each State, and the implementation of such law, whether statutory, common law, or otherwise, and whether adopted before or after the date of enactment of this Act.\n**(2) Prohibition**\nNeither the Federal Government nor any State may administer, implement, or enforce any law, rule, regulation, standard, or other provision having the force and effect of law in a manner that\u2014\n**(A)**\nprohibits or restricts the sale, provision, or use of any FDA-approved medicines (as defined in section 2(2));\n**(B)**\nprohibits or restricts any individual from aiding another individual in voluntarily obtaining or using any FDA-approved medicines; or\n**(C)**\nexempts any FDA-approved medicines from any other generally applicable law in a way that would make it more difficult to sell, provide, obtain, or use such medicines.\n**(3) Relationship with other laws**\nThis Act applies notwithstanding any other provision of Federal law, including the Religious Freedom Restoration Act of 1993 ( 42 U.S.C. 2000bb et seq. ).\n##### (b) Subsequently enacted Federal legislation\nFederal law enacted after the date of enactment of this Act is subject to this Act, unless such law explicitly excludes such application by reference to this Act.\n##### (c) Limitations\nThe provisions of this Act shall not supersede or otherwise affect any provision of Federal law relating to coverage under (and shall not be construed as requiring the provision of specific benefits under) group health plans or group or individual health insurance coverage or coverage under a Federal health care program (as defined in section 1128B(f) of the Social Security Act (42 U.S.C. 1320a\u20137b(f))), including coverage provided under section 1905(a)(4)(C) of the Social Security Act ( 42 U.S.C. 1396d(a)(4)(C) ) and section 2713 of the Public Health Service Act ( 42 U.S.C. 300gg\u201313 ).\n##### (d) Defense\nIn any cause of action against an individual or entity who is subject to a limitation or requirement that violates this Act, in addition to the remedies specified in section 7, this Act shall also apply to, and may be raised as a defense by, such an individual or entity.\n##### (e) Effective date\nThis Act shall take effect immediately upon the date of enactment of this Act.\n#### 6. Rules of construction\n##### (a) In general\nIn interpreting the provisions of this Act, a court shall liberally construe such provisions to effectuate the purposes described in section 3.\n##### (b) Rule of construction\nNothing in this Act shall be construed to authorize any government to interfere with a health care provider\u2019s ability to provide FDA-approved medicines or information related to such medicines or a patient\u2019s ability to obtain such medicines.\n##### (c) Other individuals considered as government officials\nAny individual who, by operation of a provision of Federal or State law, is permitted to implement or enforce a limitation or requirement that violates section 4 shall be considered a government official for purposes of this Act.\n#### 7. Enforcement\n##### (a) Attorney general\nThe Attorney General may commence a civil action on behalf of the United States against any State that violates, or against any government official (including an individual described in section 6(c)) that implements or enforces a limitation or requirement that violates, section 4. The court shall hold unlawful and set aside the limitation or requirement if it is in violation of this Act.\n##### (b) Private right of action\n**(1) In general**\nAny individual or entity, including any health care provider or patient, adversely affected by an alleged violation of this Act, may commence a civil action against any State that violates, or against any government official (including an individual described in section 6(c)) that implements or enforces a limitation or requirement that violates, section 4. The court shall hold unlawful and set aside the limitation or requirement if it is in violation of this Act.\n**(2) Health care provider**\nA health care provider may commence an action for relief on its own behalf, on behalf of the provider\u2019s staff, and on behalf of the provider\u2019s patients who are or may be adversely affected by an alleged violation of this Act.\n##### (c) Equitable relief\nIn any action under this section, the court may award appropriate equitable relief, including temporary, preliminary, and permanent injunctive relief.\n##### (d) Costs\nIn any action under this section, the court shall award costs of litigation, as well as reasonable attorney\u2019s fees, to any prevailing plaintiff. A plaintiff shall not be liable to a defendant for costs or attorney\u2019s fees in any nonfrivolous action under this section.\n##### (e) Jurisdiction\nThe district courts of the United States shall have jurisdiction over proceedings under this Act and shall exercise the same without regard to whether the party aggrieved shall have exhausted any administrative or other remedies that may be provided for by law.\n##### (f) Abrogation of state immunity\nNeither a State that enforces or maintains, nor a government official (including an individual described in section 6(c)) who is permitted to implement or enforce any limitation or requirement that violates section 4 shall be immune under the Tenth Amendment to the Constitution of the United States, the Eleventh Amendment to the Constitution of the United States, or any other source of law, from an action in a Federal or State court of competent jurisdiction challenging that limitation or requirement.\n#### 8. Severability\nIf any provision of this Act, or the application of such provision to any individual, entity, government, or circumstance, is held to be unconstitutional, the remainder of this Act, or the application of such provision to all other individuals, entities, governments, or circumstances, shall not be affected thereby.",
      "versionDate": "2025-07-17",
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
        "name": "Health",
        "updateDate": "2025-09-11T15:31:27Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4525ih.xml"
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
      "title": "Right to FDA-Approved Medicines Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:46Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Right to FDA-Approved Medicines Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect an individuals ability to access medicines approved by the Food and Drug Administration to protect a health care providers ability to provide such medicines, and information related to such medicines.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:24Z"
    }
  ]
}
```
