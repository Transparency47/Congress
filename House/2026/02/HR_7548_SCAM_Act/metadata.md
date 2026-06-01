# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7548?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7548
- Title: SCAM Act
- Congress: 119
- Bill type: HR
- Bill number: 7548
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-05-30T08:06:07Z
- Update date including text: 2026-05-30T08:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7548",
    "number": "7548",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001204",
        "district": "9",
        "firstName": "Daniel",
        "fullName": "Rep. Meuser, Daniel [R-PA-9]",
        "lastName": "Meuser",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "SCAM Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:07Z",
    "updateDateIncludingText": "2026-05-30T08:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:01:00Z",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "NY"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "IN"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NC"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "MI"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "MI"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "MI"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "WA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "NJ"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "NC"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NC"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "KS"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CO"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IN"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "RI"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MN"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NM"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NM"
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
      "sponsorshipDate": "2026-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "SC"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "WI"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "VA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CT"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "FL"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7548ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7548\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Meuser (for himself and Mr. Correa ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit online platforms from displaying fraudulent or deceptive commercial advertisements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Consumers from Advertising Misconduct Act or the SCAM Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOnline platforms have become a primary conduit for online scams or other digital advertising-related fraud, including fake giveaways, animal sales, deal advertisements tied to nonexistent products, government impersonations, romance scams, health scams, and impersonations using AI-cloned voices and stolen images targeting legitimate businesses.\n**(2)**\nAccording to data reported by the Federal Trade Commission, social media platforms are a primary contact method to initiate scams, with individuals ages 20 to 29 reporting social media was the contact method more than 38 percent of the time, and for individuals ages 18 to 19, that figure was 47 percent.\n**(3)**\nAccording to the Commission, the estimated overall loss from fraud in 2024, adjusted to account for underreporting, was $195,900,000,000, with an estimated $81,500,000,000 lost by older adults.\n**(4)**\nAccording to the AARP, consumers filed 2,600,000 fraud reports in 2023, with a median individual loss of $500. Nearly 100,000 consumers reported losses of $10,000 or more.\n**(5)**\nSome online platforms have abandoned tighter advertiser verification processes to avoid driving away profits from advertisers.\n**(6)**\nSection 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) was enacted to protect online platforms acting as Good Samaritans by shielding such platforms from being treated as publishers of user content, while encouraging such platforms to block or screen offensive content.\n**(7)**\nCourts have interpreted Section 230 too broadly, granting sweeping immunity even to online platforms alleged to facilitate unlawful or harmful activity and including online activities that did not exist in 1996\u2014an outcome contrary to Congress\u2019s original intent.\n**(8)**\nAccording to the Federal Trade Commission's consumer alert titled Top scams of 2024 (March 10, 2025), People reported losing money more often when contacted through social media. Most people (70 percent) reported a loss when contacted on a social media platform\u2014and lost more money overall. The Commission issued broad information requests to online platforms using the Commission\u2019s authority under section 6(b) of the Federal Trade Commission Act ( 15 U.S.C. 46(b) ) in order to assess paid advertisement screening practices, citing the surge in scam ads.\n**(9)**\nOnline platforms' inconsistent and optional efforts to mitigate the rise in scams have failed, leading to a consumer confidence crisis across digital financial systems.\n#### 3. Prohibition on digital advertising-related fraud\n##### (a) In general\nIt shall be unlawful for an online platform to display a fraudulent or deceptive commercial advertisement on such platform if the online platform\u2014\n**(1)**\naccepted payment to display such advertisement; and\n**(2)**\nfailed to take reasonable steps (as described in subsection (b)) to prevent the fraudulent or deceptive commercial advertisement from being made available.\n##### (b) Additional requirements for online platforms\n**(1) Required procedures**\nAn online platform that accepts payment, or any other form of compensation, to display an advertisement shall establish and implement procedures to require the following:\n**(A)**\nProcedures to verify the identity of each advertiser prior to the placement of a paid advertisement, including\u2014\n**(i)**\nverification of the legal name and physical location of the advertiser;\n**(ii)**\nverification of a valid and current government-issued identification of the advertiser, or, in the case of a business entity, documentation establishing the legal existence of the entity and the relation of the purchaser to the entity;\n**(iii)**\ncollection of contact information for the advertiser sufficient to allow follow up by the online platform or the Commission; and\n**(iv)**\nreasonable measures to prevent circumvention of such verification requirements through the use of any false, stolen, or synthetic identity.\n**(B)**\nAn active impersonation detection and mitigation program.\n**(C)**\nAutomated and manual fraudulent and deceptive commercial advertisement detection systems.\n**(D)**\nA clear and conspicuous tool for users to report suspected fraudulent or deceptive commercial advertisements.\n**(2) Investigation of fraudulent or deceptive commercial advertisements**\n**(A) In general**\nIf a person (including a government entity) reports a fraudulent or deceptive commercial advertisement or the detection system of an online platform identifies a fraudulent or deceptive commercial advertisement, the online platform shall\u2014\n**(i)**\nnot later than 72 hours after the submission of such report or receiving such identification, conduct an investigation of such advertisement; and\n**(ii)**\nnot later than 24 hours after concluding the investigation, if applicable, notify the person of the outcome of such investigation.\n**(B) Removal**\n**(i) After investigation**\nIf, after conducting an investigation under subparagraph (A), an online platform determines that an advertisement violates the requirements of this Act, such online platform shall, not later than 24 hours after making such determination, remove the advertisement from the platform.\n**(ii) During investigation**\nNothing in this subparagraph shall preclude an online platform from removing an advertisement prior to the conclusion of an investigation under subparagraph (A), as determined appropriate by the online platform.\n**(3) Presumed compliance**\n**(A) In general**\nFor purposes of subsection (a), an online platform shall be presumed to have taken reasonable steps to prevent a fraudulent or deceptive commercial advertisement from being made available if the online platform\u2014\n**(i)**\nsubmits to the Commission a fraudulent and deceptive commercial advertisement detection program that incorporates the procedures described in paragraph (1), and the Commission approves such program; and\n**(ii)**\ndemonstrates compliance with, and active enforcement of, the program described in clause (i), including by demonstrating that the online platform provides adequate resources for the program.\n**(B) Rule of construction**\nNothing in this paragraph shall be construed to create a presumption of compliance in any individual enforcement action in which the Commission determines or establishes that the online platform did not comply with its fraudulent and deceptive commercial advertisement detection program.\n##### (c) Regulations\n**(1) In general**\nNot later than 1 year after the date of enactment of this section, the Commission shall promulgate regulations in accordance with section 553 of title 5, United States Code, to implement this section.\n**(2) Updates**\nThe Commission shall review the regulations promulgated under paragraph (1) on an annual basis and revise such regulations as appropriate.\n##### (d) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act or a regulation promulgated under this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act and any regulation promulgated under this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates this Act or any regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (e) Enforcement by States\n**(1) Authorization**\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by the engagement of any person in an act or practice that violates subsection (a) or (b), the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in a district court of the United States of appropriate jurisdiction to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with subsection (a) or (b);\n**(C)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(D)**\nobtain such other relief as the court may consider to be appropriate.\n**(2) Rights of the Commission**\n**(A) Notice to the Commission**\n**(i) In general**\nExcept as provided in clause (iii), before initiating a civil action under paragraph (1), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring such civil action.\n**(ii) Contents**\nThe notification required by clause (i) shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required by clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention by the Commission**\nUpon receiving the notice required by subparagraph (A)(i), the Commission may intervene in the civil action and, upon intervening\u2014\n**(i)**\nbe heard on all matters arising in the civil action; and\n**(ii)**\nfile petitions for appeal of a decision in the civil action.\n**(3) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(4) Preemptive action by the Commission**\nIf the Commission has instituted a civil action for a violation of subsection (a) or (b), no State officer may bring an action under paragraph (1) during the pendency of that action against any defendant named in the complaint of the Commission for any violation of subsection (a) or (b) alleged in the complaint.\n**(5) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in the district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which the defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.\n##### (f) Private right of action\n**(1) In general**\nA person who has been injured by another person in violation of subsection (a) or (b) may bring a civil action against such person in an appropriate district court of the United States\u2014\n**(A)**\nseeking injunctive relief;\n**(B)**\nsubject to paragraph (2), to obtain actual damages; and\n**(C)**\nto obtain, for each violation, any other restitution, penalties, and other legal or equitable relief as the court may deem just and proper.\n**(2) Willful or knowing violations**\nIf the court finds that the defendant acted willfully or knowingly in committing a violation described in paragraph (1), the court may, in its discretion, increase the amount of the award to an amount equal to not more than 3 times the amount available under paragraph (1)(B).\n**(3) Costs and attorney\u2019s fees**\nThe court shall award to a prevailing plaintiff in an action under this subsection the litigation costs of such action and reasonable attorney\u2019s fees, as determined by the court.\n**(4) Limitation**\nAn action may be commenced under this subsection not later than 5 years after the date on which the person first discovered or had a reasonable opportunity to discover the violation.\n**(5) Nonexclusive remedy**\nBringing a civil action under this subsection shall be in addition to any other remedy available to the person bringing such civil action.\n##### (g) Relationship to other laws\n**(1) Effect of other laws**\n**(A) Application of section 230(c)(1)**\nSection 230(c)(1) of the Communications Act of 1934 ( 47 U.S.C. 230(c)(1) ) shall not apply to any violation of this section.\n**(B) Application of section 230(c)(2)**\nNothing in this Act shall be construed to limit or affect the civil liability protections under section 230(c)(2) of the Communications Act of 1934 ( 47 U.S.C. 230(c)(2) ).\n**(2) Effect on State laws**\nNothing in this section or any regulation promulgated under this section shall preempt or otherwise affect any State or local law.\n**(3) Severability**\nIf any provision of this section, or the application thereof to any person or circumstance, is held invalid, the remainder of this section and the application of such provision to other persons not similarly situated or to other circumstances shall not be affected by the invalidation.\n#### 4. Regulatory report on online scams and potential for additional rulemaking\n##### (a) Report required\nNot later than 9 months after the date of enactment of this section, the Commission, in consultation with other Federal agencies, shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report assessing whether additional statutory authority is needed to prevent the proliferation of online scams involving financial transactions.\n##### (b) Contents\nThe report required under subsection (a) shall include\u2014\n**(1)**\nan assessment of any regulatory gaps that allow online scams involving fraudulent advertisements or digital payment fraud to persist;\n**(2)**\nan analysis of whether improved information-sharing mechanisms between online platforms, financial institutions, and regulators could reduce consumer losses; and\n**(3)**\nrecommendations for such legislation and administrative action required to strengthen oversight of online platforms or intermediaries facilitating scam-related payments.\n#### 5. Definitions\nFor purposes of this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Deceptive**\nThe term deceptive \u2014\n**(A)**\nhas the meaning given the term in section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 );\n**(B)**\nshall be interpreted consistent with any guidance of the Commission or precedent of Federal courts applying such section; and\n**(C)**\nfor purposes of this Act, is limited to material misrepresentations, omissions, or practices that are likely to cause financial harm to a consumer.\n**(3) Online platform**\nThe term online platform means any public-facing website, online service, online application, or mobile application that predominantly provides a community forum for user-generated content, such as sharing videos, images, games, audio files, or other content, including a social media service, social network, or virtual reality environment.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-02-04",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3774",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SCAM Act",
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
        "name": "Commerce",
        "updateDate": "2026-02-26T15:50:09Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7548ih.xml"
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
      "title": "SCAM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SCAM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Consumers from Advertising Misconduct Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit online platforms from displaying fraudulent or deceptive commercial advertisements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:28Z"
    }
  ]
}
```
