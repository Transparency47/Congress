# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7238?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7238
- Title: Commission on Equity and Reconciliation in the Uniformed Services Act
- Congress: 119
- Bill type: HR
- Bill number: 7238
- Origin chamber: House
- Introduced date: 2026-01-23
- Update date: 2026-02-25T20:02:49Z
- Update date including text: 2026-02-25T20:02:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-23: Introduced in House
- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-23: Introduced in House

## Actions

- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-23",
    "latestAction": {
      "actionDate": "2026-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7238",
    "number": "7238",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000472",
        "district": "39",
        "firstName": "Mark",
        "fullName": "Rep. Takano, Mark [D-CA-39]",
        "lastName": "Takano",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Commission on Equity and Reconciliation in the Uniformed Services Act",
    "type": "HR",
    "updateDate": "2026-02-25T20:02:49Z",
    "updateDateIncludingText": "2026-02-25T20:02:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-23",
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
          "date": "2026-01-23T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-23T15:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "DC"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "WI"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "NJ"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "KS"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "KY"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "WA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "MI"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "PA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "HI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "NV"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "DE"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7238ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7238\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2026 Mr. Takano (for himself, Ms. Norton , Mr. Peters , Mr. Pocan , Ms. Simon , Mr. Gottheimer , Ms. Davids of Kansas , Mr. McGarvey , Mr. Garcia of California , Ms. Randall , Mr. Lieu , Mrs. Ramirez , Mr. Doggett , Ms. Wilson of Florida , Ms. Tlaib , Ms. Lee of Pennsylvania , Mr. Davis of Illinois , Mr. Torres of New York , Mr. Vargas , Ms. Jacobs , Mr. Case , Ms. Titus , Mr. Goldman of New York , Ms. McBride , Ms. Bonamici , and Ms. Balint ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish the Commission on Equity and Reconciliation in the Uniformed Services.\n#### 1. Short title\nThis Act may be cited as the Commission on Equity and Reconciliation in the Uniformed Services Act .\n#### 2. Establishment and duties\n##### (a) Establishment\nThere is established the Commission on Equity and Reconciliation in the Uniformed Services (in this Act referred to as the Commission ).\n##### (b) Duties\nThe Commission shall perform the following duties:\n**(1)**\nIdentify and compile a corpus of documentation on the policing of sexual orientation and gender identity in the uniformed services, from the beginning of World War II and onward. Such documentation shall include the following:\n**(A)**\nFacts related to the history of policies regarding LGBTQ+ sexual orientation and gender identity in the uniformed services.\n**(B)**\nThe effects of such policies on eligibility for, and access to, benefits under laws administered by the Secretary of Veterans Affairs on servicemembers who were discharged due to sexual orientation or gender identity.\n**(2)**\nHold public hearings in such cities of the United States as it finds appropriate, and do community outreach and other public relations efforts in order to advertise such hearings and the opportunity to give testimony.\n**(3)**\nGather testimonies, written and oral, from LGBTQ+ servicemembers and veterans about their experiences, both anonymously and with names given.\n**(4)**\nExamine the impacts that discriminatory policy and corresponding actions taken by the uniformed services had on the physical and mental wellbeing of servicemembers.\n**(5)**\nExamine lasting impacts (including psychological, financial, and professional) that policies of the uniformed services have had on veterans and servicemembers who were discharged due to their sexual orientation and/or gender identity.\n**(6)**\nExamine how discriminatory practices contributed to suicidality and homelessness among LGBTQ+ veterans.\n**(7)**\nExamine the disparate impact that policies targeting sexual and gender minorities has had on minority groups in the uniformed services, especially racial minorities and women.\n**(8)**\nExamine the impacts that policing of sexual and gender minorities has had on individuals who do not identify as LGBTQ+ but were nevertheless targeted due to perceived sexual orientation or gender identity.\n**(9)**\nExamine the impacts that discriminatory policies related to sexual orientation and gender identity have had on the dependents of servicemembers and veterans.\n**(10)**\nExamine the immediate and long-term impacts that the denial, on the bases of policies and directives of the Department of Defense and of the Department of Veteran Affairs, of medically necessary health care, including denial of treatments for gender dysphoria, has had on servicemembers and veterans.\n**(11)**\nExamine and quantify the impacts that discriminatory policies and directives of the Department of Defense related to sexual orientation and gender identity have on force readiness, including the cost of retraining and replacing individuals separated from the Armed Forces for reasons related to their real or perceived sexual orientation and/or gender identity.\n**(12)**\nCollect information on the effects of changes to individuals\u2019 demographic data (including gender markers)\u2014\n**(A)**\nin databases and systems of the Department of Defense and the Department of Veterans Affairs (including the Defense Enrollment Eligibility Reporting System);\n**(B)**\nwithout the consent of the individuals.\n**(13)**\nCollect information on\u2014\n**(A)**\nthe discharge and reentry codes under which individuals were separated from the uniformed services on the basis of the individual\u2019s real or perceived sexual orientation or gender identity; and\n**(B)**\nthe effect that such codes had on the access of servicemembers and veterans to employment and other benefits.\n**(14)**\nRecommend appropriate ways to educate the American public about institutionalized and government-sanctioned discrimination.\n**(15)**\nRecommend appropriate remedies to address the findings of the Commission, including\u2014\n**(A)**\nhow the Federal Government may offer an apology for enforcing discrimination that led to psychological, emotional, and physical harm to servicemembers and their families;\n**(B)**\nhow the Secretary of Defense may seek to properly compensate separated servicemembers\u2014\n**(i)**\nfor lost time, professional opportunities, access to benefits, and other impacts; and\n**(ii)**\nwith compensation including back pay, reinstatement, benefits reinstatement, or other opportunities;\n**(C)**\nhow the Secretary of Defense and the Secretary of Veterans Affairs can restore gender affirming services and care to servicemembers, veterans, and other beneficiaries;\n**(D)**\nhow discharge upgrades and amendments of military records may be streamlined through the Boards for Correction of Military Records, including improving the transparency and accessibility of records by the members of the Armed Forces to whom they pertain;\n**(E)**\nhow the service of LGBTQ+ individuals in the uniformed services may be made more visible in materials distributed by the Secretary of Defense and the Secretary of Veterans Affairs;\n**(F)**\nhow diversity and inclusion policies of the Department of Defense may be revised, including how resources may be committed to diversity training;\n**(G)**\nhow healthcare and other benefits, furnished by such Secretaries to members of the uniformed services and veterans, will commit more resources to meeting the needs of LGBTQ+ patients, including improved data collection on LGBTQ+ patients, mental health counseling, and other medical necessities; and\n**(H)**\nhow the Federal Government may examine the issue of burial rights denied to members of the uniformed services and veterans who were prematurely discharged due to the discriminatory policies against such members and such veterans.\n**(16)**\nThe Commission shall submit a written report of its findings to Congress not later than one year after the date of the first meeting of the Commission.\n#### 3. Membership\n##### (a) In general\nThere shall be 15 members of the Commission, who shall be appointed not later than 30 days after the date of the enactment of this Act, and as follows:\n**(1)**\nOne member appointed by the Chair of the Committee on Armed Services of the House of Representatives.\n**(2)**\nOne member appointed by the Ranking Member of the Committee on Armed Services of the House of Representatives.\n**(3)**\nOne member appointed by the Chair of the Committee on Veterans\u2019 Affairs of the House of Representatives.\n**(4)**\nOne member appointed by the Ranking Member of the Committee on Veterans\u2019 Affairs of the House of Representatives.\n**(5)**\nOne member appointed by the Chair of the Committee on Armed Services of the Senate.\n**(6)**\nOne member appointed by the Ranking Member of the Committee on Armed Services of the Senate.\n**(7)**\nOne member appointed by the Chair of the Committee on Veterans\u2019 Affairs of the Senate.\n**(8)**\nOne member appointed by the Ranking Member of the Committee on Veterans\u2019 Affairs of the Senate.\n**(9)**\nTwo members appointed by the Secretary of Defense.\n**(10)**\nTwo members appointed by the Secretary of Veterans Affairs.\n**(11)**\nOne member appointed by the Secretary of Homeland Security.\n**(12)**\nOne member appointed by the Secretary of Commerce, for the purpose of representing the National Oceanic and Atmospheric Administration.\n**(13)**\nOne member appointed by the Secretary of Health and Human Services, for the purpose of representing the Public Health Service.\n##### (b) Qualifications\nAll members of the Commission shall be persons who are exceptionally qualified to serve on the Commission by virtue of their education, training, activism, or experience, particularly in the fields of advocating for LGBTQ+ members of the uniformed services.\n##### (c) Terms\nThe term of office for members shall be for the life of the Commission. A vacancy in the Commission shall not affect the powers of the Commission and shall be filled in the same manner in which the original appointment was made.\n##### (d) First meeting\nThe President shall call the first meeting of the Commission not later than 30 days after the later of the following:\n**(1)**\nThe date of the enactment of this Act.\n**(2)**\nThe date of the enactment of an Act that makes appropriations to carry out this Act.\n##### (e) Quorum\nEight members of the Commission shall constitute a quorum, but a lesser number may hold hearings.\n##### (f) Chair and Vice Chair\nThe Commission shall elect a Chair and Vice Chair from among its members. The term of office for each shall be for the life of the Commission.\n##### (g) Compensation\n**(1) In general**\nEach member of the Commission may be compensated at a rate not to exceed the daily equivalent of the annual rate of basic pay in effect for a position at level IV of the Executive Schedule under section 5315 of title 5, United States Code, for each day during which that member is engaged in the actual performance of the duties of the Commission.\n**(2) Federal employees**\nA member of the Commission who is a full-time officer or employee of the United States or a Member of Congress shall receive no additional pay, allowances, or benefits by reason of the member\u2019s service to the Commission.\n**(3) Travel expenses**\nEach member shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code.\n#### 4. Powers of the Commission\n##### (a) Hearings and sessions\nThe Commission may, for the purpose of carrying out the provisions of this Act, hold such hearings and sit and act at such times and at such places in the United States, and request the attendance and testimony of such witnesses and the production of such books, records, correspondence, memoranda, papers, and documents, as the Commission considers appropriate. The Commission may invoke the aid of an appropriate United States district court to require, by subpoena or otherwise, such attendance, testimony, or production.\n##### (b) Powers of subcommittees and members\nAny subcommittee or member of the Commission may, if authorized by the Commission, take any action which the Commission is authorized to take under this section.\n##### (c) Obtaining official data\nThe Commission may acquire directly from the head of any department, agency, or instrumentality of the executive branch of the Federal Government, available information which the Commission considers useful in the discharge of its duties. All departments, agencies, and instrumentalities of the executive branch of the Government shall cooperate with the Commission with respect to such information and shall furnish all information requested by the Commission to the extent permitted by law.\n#### 5. Administrative provisions\n##### (a) Staff\nThe Commission may, without regard to the civil service laws and regulations, appoint and fix the compensation of such personnel as the Commission considers appropriate.\n##### (b) Applicability of certain civil service laws\nThe personnel of the Commission may be appointed without regard to the provisions of title, United States Code, governing appointments in the competitive service, and without regard to the provisions of chapter 51 and subchapter III of chapter 53 of such title, relating to classification and General Schedule pay rates, except that the rate of basic pay of any employee of the Commission may not exceed the rate of basic pay established for a position at level V of the Executive Schedule under section 5316 of such title.\n##### (c) Experts and consultants\nThe Commission may procure the services of experts and consultants in accordance with the provisions of section 3109(b) of title 5, United States Code, but at rates for individuals not to exceed the daily equivalent of the annual rate of basic pay established for a position at level V of the Executive Schedule under section 5316 of such title.\n##### (d) Administrative support services\nThe Commission may enter into agreements with the Administrator of General Services for procurement of financial and administrative services necessary for the discharge of the duties of the Commission. Payment for such services shall be made by reimbursement from funds of the Commission in such amounts as may be agreed upon by the Chairman of the Commission and the Administrator.\n##### (e) Contracts\nThe Commission may\u2014\n**(1)**\nprocure supplies, services, and property by contract in accordance with applicable laws and regulations and to the extent or in such amounts as are provided in appropriations Acts; and\n**(2)**\nenter into contracts with departments, agencies, and instrumentalities of the Federal Government, State agencies, and private firms, institutions, and agencies, for the conduct of research or surveys, the preparation of reports, and other activities necessary for the discharge of the duties of the Commission, to the extent or in such amounts as are provided in appropriations Acts.\n#### 6. Termination\n##### (a) In general\nThe Commission, and all the authorities of this title, shall terminate 90 days after the date on which the final report is submitted under section 2.\n##### (b) Administrative activities before termination\nThe Commission may use the 90-day period referred to in subsection (a) for the purpose of concluding its activities, including providing testimony to committees of Congress concerning its reports and disseminating the final report.\n#### 7. Funding\n##### (a) In general\nThere is authorized to be appropriated such sums as necessary to carry out this Act.\n##### (b) Duration\nAmounts made available to the Commission under subsection (a) shall remain available until the termination of the Commission.\n#### 8. Definitions\nIn this Act:\n**(1)**\nThe term servicemember has the meaning given such term in section 101 of the Servicemembers Civil Relief Act ( 50 U.S.C. 3911 ).\n**(2)**\nThe term uniformed services has the meaning given such term in section 101 of title 10, United States Code.",
      "versionDate": "2026-01-23",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-01-27",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3691",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Commission on Equity and Reconciliation in the Uniformed Services Act",
      "type": "S"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-13T18:26:48Z"
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
      "date": "2026-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7238ih.xml"
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
      "title": "Commission on Equity and Reconciliation in the Uniformed Services Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commission on Equity and Reconciliation in the Uniformed Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Commission on Equity and Reconciliation in the Uniformed Services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:37Z"
    }
  ]
}
```
