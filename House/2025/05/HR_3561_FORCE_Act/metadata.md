# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3561?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3561
- Title: FORCE Act
- Congress: 119
- Bill type: HR
- Bill number: 3561
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-02-04T05:06:16Z
- Update date including text: 2026-02-04T05:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3561",
    "number": "3561",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "FORCE Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:16Z",
    "updateDateIncludingText": "2026-02-04T05:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3561ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3561\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Nunn of Iowa (for himself and Mr. Himes ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo establish a National Defense Executive Reserve, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Overhaul of Reserve Command Executive Modernization Act or the FORCE Act .\n#### 2. National Defense Executive Reserve\n##### (a) In general\nTitle VII of the Defense Production Act of 1950 ( 50 U.S.C. 4551 et seq. ) is amended by inserting after section 711 the following:\n712. National Defense Executive Reserve (a) Establishment The President shall establish a National Defense Executive Reserve (in this section referred to as the Reserve ). (b) Purpose The purpose of the Reserve shall be to\u2014 (1) improve the preparedness of the Federal Government for national defense emergencies by allowing private persons with unique expertise to volunteer, be trained for and temporarily employed in Federal positions within any of the Federal agencies that has established a Reserve unit under subsection (c) that may be necessary during an national defense emergency; (2) efficiently augment the capabilities of the Federal Government with these private persons as required during periods of national defense emergency when activated by the President; (3) provide a cost-efficient way of expanding Federal Government capacity for the management of future national defense emergencies without needing to dramatically expand the number of full-time Federal employees; and (4) enable the appropriate controls and oversight to be established by the Federal Government in advance of the activation of the Reserve to avoid real or perceived conflicts of interest or other harms created by the temporary employment of private persons who volunteer to be temporarily employed by the Reserve. (c) Reserve units (1) In general The President shall require the heads of each of the following agencies to establish a unit of the Reserve within the applicable agency: (A) The Department of Commerce. (B) The Department of Defense. (C) The Department of Homeland Security. (D) Such other agencies as the President determines appropriate. (2) Deadline The units of the Reserve within the agencies described under subparagraphs (A), (B), and (C) shall be established not later than 180 days after the issuance of the final rules required under subsection (f). (d) Activation The President may only activate a unit of the Reserve\u2014 (1) on non-delegable basis; (2) during a national emergency declared by the President under the National Emergencies Act ( 50 U.S.C. 1601 et seq. ) with respect to which the President has specified, as described under section 301 of such Act, that the President may activate the Reserve pursuant to the authorities under this section; and (3) upon a public determination by the President that the activation is necessary to support the national defense. (e) Training The President may, without activating the Reserve, allow for periodic training and exercises to prepare the Reserve for duty during an activation. (f) Rulemaking Not later than 270 days after the date of enactment of this section, the Director of the Office of Personnel Management, in consultation with the Secretary of Commerce, the Secretary of Defense, and the Secretary of Homeland Security, shall issue rules, in accordance with section 553 of title 5, United States Code, to provide\u2014 (1) instruction on\u2014 (A) criteria for determining the number of positions in and organization of Reserve units; (B) criteria for determining the appropriate level of seniority and job classifications of Reserve positions; (C) the advertisement of the Reserve to the public to generate interest in volunteers; (D) the selection of individuals for the Reserve and the job assignment process; (E) the appointment authorities to be used by the head of an agency during an activation of the applicable Reserve unit; (F) the appropriate levels of compensation for private individuals for service in the Reserve, dependent on the qualifications and expected roles of the individuals; (G) the appropriate levels of compensation for private individuals for service in the Reserve for additional expenses, such as travel and accommodation, to fulfill the responsibilities in the Reserve, including during training and exercise; (H) additional incentives to be provided to private individuals to encourage participation in the Reserve; (I) whether and how to issue security clearances to individuals selected to serve in the Reserve, both prior to and during activation; (J) the frequency and content of training and exercises for the Reserve; (K) the appropriate interaction between permanent Government employees and individuals in the Reserve during training, exercises, and activations of the Reserve; (L) the appointment of permanent Government employees to manage the Reserve for each agency with a Reserve unit, both prior to and during activation; (M) all other matters necessary to effectively manage the Reserve, as determined by the Director of the Office of Personnel Management; and (2) recommendations and considerations for the President on selective activation of the Reserve. (g) Additional guidance The Director of the Office of Personnel Management may issue any additional internal guidance as the Director of the Office of Personnel determines is necessary to supplement the rules issued under subsection (f). (h) Employment protection For purposes of chapter 43 of title 38, United States Code, an individual absent from a position of employment due to an appointment into service in the Reserve shall be subject to the same employment and reemployment protections as are provided under such chapter for an individual absent from a position of employment due to an appointment into service in the Federal Emergency Management Agency as intermittent personnel under section 306(b)(1) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act. .\n##### (b) Funding\nSection 304(c) of the Defense Production Act of 1950 ( 50 U.S.C. 4534(c) ) is amended by inserting and section 712 after this title .\n##### (c) Conforming amendment\nSection 710 of the Defense Production Act of 1950 ( 50 U.S.C. 4560 ) is amended\u2014\n**(1)**\nby striking subsection (e); and\n**(2)**\nby redesignating subsections (f) and (g) as subsections (e) and (f), respectively.\n#### 3. Improving the use of voluntary agreements\n##### (a) In general\nSection 708 of the Defense Production Act of 1950 ( 50 U.S.C. 4558 ) is amended\u2014\n**(1)**\nby striking subsection (c)(2) and inserting the following: The authority granted to the President in paragraph (1) and subsection (d) may be delegated by him to the head of any Federal agency to which the President has delegated authority under this Act. ;\n**(2)**\nby striking subsection (c)(3);\n**(3)**\nin subsection (d)(2), by striking and the Federal Trade Commission. ;\n**(4)**\nby striking subsection (e) and inserting the following:\n(e) Rulemaking relating to voluntary agreements (1) In general The Secretary of Commerce issue rules, after approval of the Attorney General, in accordance with section 553 of title 5, United States Code, that incorporate standards and procedures by which voluntary agreements and plans of action may be developed and carried out. (2) Publication requirement Notwithstanding section 553 of title 5, United States Code, the Secretary of Commerce shall publish any rule issued under paragraph (1) in the Federal Register not less than 30 days before the effective date of such rule. .\n**(5)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (1)(B)\u2014\n**(i)**\nstriking by (after consultation with the Chairman of the Federal Trade Commission) ; and\n**(ii)**\nstriking by and publishes such a finding in the Federal Register ; and\n**(B)**\nin paragraph (2), by striking (after consultation with the Chairman of the Federal Trade Commission) ;\n**(6)**\nin subsection (g), by striking and the Chairman of the Federal Trade Commission and inserting and the Secretary of Commerce ;\n**(7)**\nin subsection (h)\u2014\n**(A)**\nin subparagraph (2), by striking and the Chairman of the Federal Trade Commission ;\n**(B)**\nin subparagraph (3), by striking , or the Chairman of the Federal Trade Commission in both places it appears;\n**(C)**\nin subparagraph (4), by striking and the Chairman of the Federal Trade Commission ;\n**(D)**\nby striking paragraphs (6), (7), (8), (10), and (11) and redesignating paragraph (9) as paragraph (6);\n**(E)**\nin subparagraph (6)(A), as so redesignated, by striking the Chairman of the Federal Trade Commission and ; and\n**(F)**\nin subparagraph (6)(B), as so redesignated, by striking and the Chairman of the Federal Trade Commission .\n**(8)**\nby striking subsection (i) and inserting the following:\n(i) Rules The Attorney General shall, not later than 270 days after the date of the enactment of this subsection, issue a rule, in accordance with section 553 of title 5, United States Code, that establishes how the Attorney General shall carry out the responsibilities of the Attorney General under this section in a manner that maintains a proper balance between providing for the national defense and protecting competition and preventing anticompetitive practices and effects from the creation and implementation of voluntary agreements and their plans of action. ; and\n**(9)**\nin subsection (k)\u2014\n**(A)**\nby striking and the Federal Trade Commission ; and\n**(B)**\nby striking (after consultation with the Federal Trade Commission) ; and\n**(10)**\nin subsection (m)\u2014\n**(A)**\nby striking (d)(2), ; and\n**(B)**\nby striking (7), and (8), .\n##### (b) Required development of voluntary agreement\n**(1) In general**\nNot later than the later of the date that is 18 months after the date of the enactment of this Act and the date on which the Attorney General issues a rule under Section 708(i) of the Defense Production Act of 1950, the President shall develop a voluntary agreement under section 708 of the Defense Production Act.\n**(2) Requirements**\nThe voluntary agreement entered by the President under paragraph (1) shall\u2014\n**(A)**\naddress a current critical national defense issue, such as\u2014\n**(i)**\nthe need for a plan of action to respond to a catastrophic cyber attack on a sector of critical infrastructure, as defined in section 5195c(e) of title 42, United States Code, including how to restore that sector as quickly as possible from the attack through public and private cooperation; or\n**(ii)**\nanother issue pertinent to national defense as determined by the President and notified to Congress within 270 days of enactment of this Act; and\n**(B)**\nuse 1 or more of the units of the National Defense Executive Reserve established under section 712 of the of the Defense Production Act of 1950.",
      "versionDate": "2025-05-21",
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
        "name": "Emergency Management",
        "updateDate": "2025-06-23T17:27:12Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3561ih.xml"
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
      "title": "FORCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FORCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Overhaul of Reserve Command Executive Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a National Defense Executive Reserve, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T04:18:22Z"
    }
  ]
}
```
