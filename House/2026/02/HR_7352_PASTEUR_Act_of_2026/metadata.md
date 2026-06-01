# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7352?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7352
- Title: PASTEUR Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7352
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-05-15T08:08:25Z
- Update date including text: 2026-05-15T08:08:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7352",
    "number": "7352",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "PASTEUR Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-15T08:08:25Z",
    "updateDateIncludingText": "2026-05-15T08:08:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-04T15:01:30Z",
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
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NC"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "AL"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NJ"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "NE"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NE"
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
      "sponsorshipDate": "2026-03-12",
      "state": "NY"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NJ"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IN"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "GA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MD"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7352ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7352\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Carter of Georgia (for himself, Mr. Peters , Mr. Langworthy , Mr. Levin , and Mr. Carey ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Public Health Service Act to establish a program to develop innovative antimicrobial drugs targeting the most challenging pathogens and most threatening infections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pioneering Antimicrobial Subscriptions To End Upsurging Resistance Act of 2026 or the PASTEUR Act of 2026 .\n#### 2. Purpose\nThe purpose of this Act is to ensure the availability of antimicrobials to\u2014\n**(1)**\nstimulate a new age of research, development, and market access to lifesaving medicines;\n**(2)**\nensure the appropriate use of lifesaving medicines;\n**(3)**\nmaintain the highest medical care standards for American patients;\n**(4)**\npromote national health system preparedness; and\n**(5)**\ndefend the United States and its military.\n#### 3. Developing antimicrobial innovations\nTitle III of the Public Health Service Act ( 42 U.S.C. 241 et seq. ) is amended by adding at the end the following:\nX U.S. NOVEL ANTIMICROBIAL SUPPLY CONTRACTS 399PP. Contract application, award, and implementation (a) In general The Secretary may enter into contracts with sponsors of eligible antimicrobials for the purpose of ensuring the availability of such eligible antimicrobials. (b) Eligible antimicrobial To be eligible for a contract under this section, an antimicrobial drug shall\u2014 (1) treat a pathogen\u2014 (A) included as an urgent or serious threat in the most recent Antibiotic Resistance Threats in the United States report published by the Centers for Disease Control and Prevention; or (B) that the Secretary has determined appropriate in consultation with the Advisory Group established under section 399PP\u20131; and (2) address an unmet medical need. (c) Applications (1) Submission To be eligible to enter into a contract under this section, a sponsor of an eligible antimicrobial shall submit to the Secretary an application not later than 2 years after the date on which the eligible antimicrobial is\u2014 (A) approved under section 505(c) of the Federal Food, Drug, and Cosmetic Act (including in accordance with section 506(h) of such Act); or (B) licensed under section 351(a) of this Act. (2) Contents An application submitted under paragraph (1) with respect to an eligible antimicrobial\u2014 (A) shall include\u2014 (i) appropriate information to determine the score of the eligible antimicrobial in accordance with the methodology established under subsection (d); and (ii) such other information as the Secretary determines appropriate; and (B) is not required to include information relating to pricing or research and development costs of the eligible antimicrobial. (3) Review Not later than 90 days after the date on which the Secretary receives an application under this subsection with respect to an eligible antimicrobial (including a revised application under paragraph (4)), the Secretary shall\u2014 (A) review the application; (B) if the eligible antimicrobial\u2019s score is below the minimum scoring threshold described in subsection (d)(1)(B), deny the application; and (C) if the eligible antimicrobial\u2019s score meets or exceeds such minimum scoring threshold, approve the application and calculate annual payments for the contract under subsection (f). (4) Revised applications Beginning 1 year after the denial of an application with respect to an eligible antimicrobial under paragraph (3), and not more frequently than once every 2 years thereafter, the sponsor of the eligible antimicrobial may submit to the Secretary a revised application for the eligible antimicrobial with additional information that may materially affect the eligible antimicrobial\u2019s score under subsection (d). (d) Scoring (1) In general Not later than 270 days after the date of enactment of this part, the Secretary, in consultation with the Advisory Group established under section 399PP\u20131, the Assistant Secretary for Preparedness and Response, the Director of the Biomedical Advanced Research and Development Authority, and the Commissioner of Food and Drugs, shall promulgate regulations, after the consideration of comments received in response to a public request for information and a public hearing, establishing\u2014 (A) a quantitative scoring methodology for eligible antimicrobials for which applications are submitted under this section; and (B) a minimum scoring threshold that the score of an eligible antimicrobial under paragraph (2) must meet or exceed in order for the sponsor of such eligible antimicrobial to enter into a contract under this section. (2) Methodology An eligible antimicrobial shall receive a score, calculated by points awarded based on criteria developed in consultation with the Advisory Group established under section 399PP\u20131 within the following three categories, with a weighting assigned to each criterion established under such categories and a greater number of points resulting in a higher score: (A) Category i The eligible antimicrobial\u2019s major contributions to patient care, including\u2014 (i) improving clinical outcomes for patients with multi-drug-resistant infections; (ii) improved dose frequency; (iii) reduced toxicity; (iv) reductions in adverse events; and (v) benefits from the eligible antimicrobial\u2019s route of administration, especially through oral administration or more than one administration method. (B) Category ii The innovative characteristics of the eligible antimicrobial, including\u2014 (i) being a first-approved antimicrobial drug that has the potential to address, or has the evidence of addressing, unmet medical needs for the treatment of a serious or life-threatening infection, or, to a lesser extent, second and third drugs that treat such infection; (ii) containing no active moiety (as defined in section 314.3 of title 21, Code of Federal Regulations (or any successor regulations)) that has been approved in any other application under section 505(b) of the Federal Food, Drug, and Cosmetic Act and containing no active ingredient licensed in any other biological product license application under section 351(a) of this Act; (iii) being a member of a new class of drugs with a novel target or novel mode of action that are distinctly different from the target or mode of any antimicrobial drug approved under such section 505(b) or licensed under such section 351(a); and (iv) addressing a multi-drug resistant infection through a novel chemical scaffold or mode of action. (C) Category iii The benefit of the eligible antimicrobial to health systems and public health, including\u2014 (i) not being affected by cross-resistance to one or more antimicrobials approved under such section 505(b) or licensed under such section 351(a); (ii) manufacturing capabilities within the United States; (iii) improved product stability and storage; (iv) increased activity against resistance mechanisms; and (v) reduction of the economic or population burden of antimicrobial resistance in the United States. (e) Contract requirements As a condition of entering into a contract under this section with respect to an eligible antimicrobial, the sponsor of the eligible antimicrobial shall\u2014 (1) beginning on the date that is 30 days after the sponsor receives its first payment under the contract and for the remainder of the contract term, ensure\u2014 (A) the commercial availability of the eligible antimicrobial in the United States; and (B) sufficient supply of the eligible antimicrobial for antimicrobial susceptibility test device manufacturers; (2) identify, track, and publicly report drug resistance data and trends using available data related to the eligible antimicrobial, including the use of data collected by the Secretary under section 399PP\u20132(c); (3) develop and implement education and communications strategies for health care professionals and patients concerning the appropriate use of the eligible antimicrobial, such as\u2014 (A) information from labeling approved by the Food and Drug Administration; and (B) communications for individuals with limited English proficiency and individuals with disabilities; (4) submit to the Secretary a plan regarding the appropriate use of the eligible antimicrobial, including best practices for antimicrobial stewardship and a general description of how the product will be marketed. The appropriate use plan may include a plan to collect data on the impact of diagnostics, antimicrobial stewardship programs, and other appropriate use efforts on patient outcomes and health-care costs; (5) upon the request of the Secretary, submit to the Secretary a plan for registering the eligible antimicrobial in countries other than the United States where an unmet medical need exists; (6) undertake efforts to ensure a reliable drug supply chain, including, in the event of the Food and Drug Administration determining that a shortage exists for the eligible antimicrobial, not later than 30 days after such determination submitting to the Secretary a plan to address such shortage; (7) beginning on the date that is 30 days after the sponsor receives its first payment under the contract and for the remainder of the contract term, manufacture the eligible antimicrobial drug at a volume that reasonably ensures the availability of sufficient quantities of the drug to meet the needs of individuals with the disease or condition for which the eligible antimicrobial is approved in the United States; (8) abide by manufacturing and environmental best practices for the control of discharge of antimicrobial active pharmaceutical ingredients and other antimicrobial agents or products, including the antibiotic manufacturing standard developed by the AMR Industry Alliance (as described in the report titled Minimizing risk of developing antibiotic resistance and aquatic ecotoxicity in the environment resulting from the manufacturing of human antibiotics published in May 2025) or seeking a sustainability certification from BSI Standards Limited; and (9) abide by such other terms as the Secretary may require under the contract. (f) Annual payments (1) In general Pursuant to a contract entered into under this section, the Secretary shall make annual payments to the sponsor of an eligible antimicrobial for the duration of the contract term. Such payments shall begin not later than 180 days after the date on which the Secretary approves the contract. (2) Calculation system The Secretary, in consultation with the Administrator of the Centers for Medicare & Medicaid Services, shall promulgate regulations establishing a system for the calculation of the annual payments described in paragraph (1). Such system shall adhere to the following: (A) Minimum and maximum amount An annual payment may not be less than $75,000,000 or more than $300,000,000, adjusted on an annual basis in accordance with the consumer price index for all urban consumers (all items; United States city average). (B) Adjustment for net revenue The annual payment shall be adjusted downward by the amount of net revenue from sales in the United States of the eligible antimicrobial during the previous 12-month period, including any legally mandated or voluntary discounts and rebates provided by the sponsor of the eligible antimicrobial, such as volume discounts, prompt pay discounts, cash discounts, free goods that are contingent on any purchase requirement, chargebacks, and rebates. (3) Disclosure of information The Secretary may require the sponsor of an eligible antimicrobial to disclose to the Secretary such information as the Secretary requires to calculate an annual payment under this subsection. Notwithstanding any other provision of law, such information shall be kept confidential and may not be\u2014 (A) disclosed by the Secretary to any entity, including other governmental or private parties, in a form that reveals the identity of a specific manufacturer or the prices charged for drugs by such manufacturer; or (B) used by the Secretary for any purpose other than calculating the annual payments under this subsection. (4) Termination of payments The Secretary may cease annual payments pursuant to a contract entered into under this section if the Secretary determines that the sponsor of the eligible antimicrobial subject to such contract\u2014 (A) permanently withdraws the eligible antimicrobial from the market in the United States; (B) materially fails to meet one or more of the requirements described in subsection (e) after notice by the Secretary and an opportunity to correct; or (C) does not conduct with due diligence a postmarket study required to be completed by the Food and Drug Administration during the term of the contract. (5) Rule of construction Nothing in this subsection shall be construed as authorizing the Secretary\u2014 (A) to disclose any information that is a trade secret or confidential information subject to section 552(b)(4) of title 5, United States Code, or section 1905 of title 18, United States Code; or (B) to use evidence from comparative clinical effectiveness research in a manner that treats extending the life of an elderly, disabled, or terminally ill individual as of lower value than extending the life of an individual who is younger, nondisabled, or not terminally ill for the purposes of calculating annual payments under this subsection, including in such a way that would limit patient access. (g) Contract term (1) Length of term The term of a contract entered into under this section shall end on the earlier of\u2014 (A) the date that is 10 years after the date on which the contract is approved; and (B) the date on which the Secretary determines at least one drug or biological product is\u2014 (i) approved or licensed (as applicable)\u2014 (I) under section 505(j) of the Federal Food, Drug, and Cosmetic Act, using the contract antimicrobial as the listed drug; or (II) under section 351(k) of the Public Health Service Act, using the contract antimicrobial as the reference product; and (ii) marketed pursuant to such approval or licensure. (2) Effect A contract shall remain in effect for the term described in paragraph (1) even if the pathogen treated by the eligible antimicrobial is later removed from the Antibiotic Resistance Threats in the United States report described in subsection (b)(1)(A). (h) Other government participation The Secretary shall make efforts to increase the participation of other governmental bodies in offering financial incentives to create commercial access to new and novel antimicrobials that are similar to the contracts under this section. (i) Authority vested in the secretary The authority vested in the Secretary by this section to enter into contracts may be performed without regard to such provisions of law or regulations relating to the making, performance, amendment, or modification of contracts of the United States, as the Secretary may determine to be inconsistent with the furtherance of the purposes of this part. 399PP\u20131. Critical need antimicrobial advisory group (a) In general Not later than 60 days after the date of enactment of this part, the Secretary shall establish a Critical Need Antimicrobial Advisory Group (referred to in this part as the Advisory Group ) and appoint its members. (b) Members The Advisory Group shall be composed of 15 members, to be appointed by the Secretary as follows: (1) 4 individuals who are physicians board-certified in infectious diseases. (2) 4 individuals who are experts with demonstrated expertise in antimicrobial resistance, health economics, or research and development or commercialization of antimicrobial drugs. (3) 4 individuals to serve as patient advocates, who are well versed in antimicrobial treatment or resistance, either as patients themselves or as caretakers. (4) 3 additional individuals who meet the qualifications specified in paragraph (1), (2), or (3). (c) Chair In addition to the members appointed under subsection (b), the Secretary shall appoint 1 individual to serve as a non-voting Chair of the Advisory Group. Such individual shall meet the qualifications specified in paragraph (1), (2), or (3) of subsection (b). (d) Conflicts of interest In appointing members under subsection (b) and a Chair under subsection (c), the Secretary shall ensure that no member (including the Chair) receives during the individual\u2019s term of service with the Advisory Group compensation in any manner from a commercial or for-profit entity that develops or intends to develop antimicrobial drugs. In implementing the requirements of this part, the Secretary shall prohibit Advisory Group members (including the Chair) from participating in any particular Advisory Group matter that will have a direct and predictable effect on their financial interests. (e) Applicability of FACA (1) In general Except as otherwise provided in this section, chapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ) shall apply to the Advisory Group. (2) Termination Section 1013 of such title (relating to the termination of advisory committees) shall not apply to the Advisory Group. 399PP\u20132. Encouraging appropriate use of antimicrobials and combating resistance (a) Health facility grant program (1) In general Not later than 1 year after the date of enactment of this part, the Secretary, acting through the Director of the Centers for Disease Control and Prevention (in this subsection referred to as the Secretary ), shall establish a grant program to support hospital, skilled nursing facility, and other health care facility efforts\u2014 (A) to judiciously use antimicrobial drugs, such as by establishing or implementing appropriate use programs, including infectious disease telehealth programs, using appropriate diagnostic tools, partnering with academic hospitals, increasing health care-associated infection reporting and prevention efforts, and monitoring antimicrobial resistance; and (B) to participate in the National Healthcare Safety Network Antimicrobial Use and Resistance Module or the Emerging Infections Program Healthcare-Associated Infections Community Interface activity of the Centers for Disease Control and Prevention, as specified by the Secretary, relating to antimicrobial drugs. (2) Prioritization In awarding grants under paragraph (1), the Secretary shall prioritize health care facilities without an existing program to judiciously use antimicrobial drugs, subsection (d) hospitals (as defined in section 1886(d)(1)(B) of the Social Security Act) that are located in rural areas (as defined in section 1886(d)(2)(D) of such Act), critical access hospitals (as defined in section 1861(mm)(1) of such Act), hospitals serving Tribal populations, and safety-net hospitals. (3) Standards for use of grant funds In implementing or expanding an antibiotic stewardship program, an entity receiving a grant under paragraph (1) shall adhere to nationally recognized guidelines and best practices, including adequate staffing, for improving antibiotic use. (b) Antimicrobial stewardship pilot program for outpatient facilities (1) Antimicrobial stewardship pilot program for outpatient facilities Not later than 2 years after the date of enactment of this part, the Secretary, in consultation with the Director of the Centers for Disease Control and Prevention and the Administrator of the Centers for Medicare & Medicaid Services (in this subsection referred to as the Secretary ), shall establish a pilot program to make grants to entities to implement or expand antibiotic stewardship programs in outpatient facilities. (2) Implementation In developing the pilot program, the Secretary shall consult with professional societies with expertise in antibiotic stewardship. (3) Eligible entities To be eligible to receive a grant under paragraph (1), an entity shall be\u2014 (A) a physician; (B) a hospital outpatient department; (C) an urgent care setting described in paragraph (5)(A); or (D) a retail clinic described in paragraph (5)(B). (4) Standards for use of grant funds In implementing or expanding an antibiotic stewardship program through a grant under this subsection, an entity shall adhere to nationally recognized guidelines and best practices, including adequate staffing, for improving antibiotic use. (5) Prioritization In awarding grants under paragraph (1), the Secretary shall prioritize\u2014 (A) urgent care settings, such as facilities that use Place of Service Code 20 for urgent care developed by the Centers for Medicare & Medicaid Services (or any successor code); and (B) retail clinics, meaning facilities that are co-located with a pharmacy or other retail commercial establishment, such as those that use Place of Service Code 17 for walk-in retail health clinics developed by the Centers for Medicare & Medicaid Services (or any successor code). (6) Report Not later than 5 years after the date of enactment of this part, the Secretary shall submit to Congress a report on the impacts of the pilot program, including recommendations for expanding antimicrobial stewardship to additional outpatient settings. (c) Surveillance and reporting of antimicrobial use and resistance (1) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall use the National Healthcare Safety Network and other appropriate surveillance systems to collect data and assess trends in antimicrobial resistance and antibiotic and antifungal use, such as\u2014 (A) appropriate conditions and measures causally related to antimicrobial resistance, including types of infections, the source or body sites of infections, the demographic information of patients with infections, infection onset in a community or hospital setting, increased lengths of hospital stay, increased costs, and rates of mortality; and (B) changes in bacterial and fungal resistance to antimicrobial drugs, including changes in percent resistance, prevalence of antimicrobial-resistant infections, rates of mortality, and other such changes. (2) Antimicrobial use data The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall obtain reliable and comparable human antibiotic and antifungal drug consumption data (including, as available and appropriate, volume antimicrobial distribution data and antibiotic and antifungal use data, including prescription data) by State or metropolitan areas. To accomplish this, the Secretary may work with, as appropriate, Federal departments and agencies (including the Department of Veterans Affairs, the Department of Defense, the Department of Homeland Security, the Bureau of Prisons, the Indian Health Service, and the Centers for Medicare & Medicaid Services), private vendors, health care organizations, pharmacy benefit managers, and other entities. (3) Antimicrobial resistance trend data The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall intensify and expand efforts to collect antimicrobial resistance data and encourage adoption of the Antimicrobial Use and Resistance Module or other appropriate module within the National Healthcare Safety Network and other appropriate surveillance systems among all health care facilities across the continuum of care, including, as appropriate, acute care hospitals, dialysis facilities, nursing homes, ambulatory surgical centers, and other ambulatory health care settings in which antimicrobial drugs are routinely prescribed. The Secretary shall seek to collect such data from electronic medication administration reports and laboratory systems to produce the reports described in paragraph (5). (4) Diagnostics data The Secretary shall collect data on tests used to diagnose and inform the appropriate treatment of infections in health care settings. This includes data on the implementation of diagnostic stewardship to ensure the appropriate use of a diagnostic test before a treatment is prescribed, and the use of diagnostics in monitoring and tracking infectious diseases. The Secretary shall collect data on the use of diagnostic tests through the National Healthcare Safety Network (in this paragraph referred to as the NHSN ) Antimicrobial Use and Resistance Module or other appropriate NHSN module. These efforts shall be implemented in collaboration with external stakeholders, including infectious disease professional societies, patient advocacy organizations, health care systems and professionals, and the diagnostics industry. (5) Public availability of data Beginning on the date that is 2 years after the date of enactment of this part, the Secretary shall, for the purposes of improving the monitoring of important trends in antimicrobial use and resistance, and, as appropriate, patient outcomes in relation to antimicrobial resistance\u2014 (A) make the data described in paragraphs (1) through (4) publicly available through reports and web updates issued on a regular basis that is not less than annually; and (B) examine opportunities to make such data available in near real time. 399PP\u20133. Definitions In this part: (1) Antimicrobial drug The term antimicrobial drug \u2014 (A) means\u2014 (i) a drug that directly inhibits replication of or kills bacteria or fungi, or acts on the substances produced by such bacteria or fungi, relevant to the proposed indication at concentrations likely to be attainable in humans to achieve the intended therapeutic effect; and (ii) a biological product that acts directly on bacteria or fungi or on the substances produced by such bacteria or fungi; and (B) does not include\u2014 (i) a drug that achieves the effect described in subparagraph (A)(i) only at a concentration that cannot reasonably be studied in humans because of its anticipated toxicity; or (ii) a vaccine. (2) Contract The term contract means a transaction other than a procurement contract, grant, or a cooperative agreement. (3) Contract antimicrobial The term contract antimicrobial means an antimicrobial drug or biological product for which a contract under this part is in effect. (4) Eligible antimicrobial The term eligible antimicrobial means an antimicrobial drug or biological product that satisfies the eligibility criteria described in section 399PP(b). 399PP\u20134. Appropriations (a) In general To carry out this part, there is authorized to be appropriated, and appropriated, to the Secretary, out of amounts in the Treasury not otherwise appropriated, $6,000,000,000 for fiscal year 2026, to remain available until expended. (b) Allocation The Secretary may use not more than 6.5 percent of the amounts appropriated under subsection (a) to carry out section 399PP\u20132. (c) Emergency designation (1) In general The amounts provided by this section are designated as an emergency requirement pursuant to section 4(g) of the Statutory Pay-As-You-Go Act of 2010. (2) Designation in senate In the Senate, this section is designated as an emergency requirement pursuant to section 4112(a) of H. Con. Res. 71 (115th Congress), the concurrent resolution on the budget for fiscal year 2018. .",
      "versionDate": "2026-02-04",
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
        "updateDate": "2026-03-09T14:18:14Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7352ih.xml"
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
      "title": "PASTEUR Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PASTEUR Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-06T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pioneering Antimicrobial Subscriptions To End Upsurging Resistance Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-06T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to establish a program to develop innovative antimicrobial drugs targeting the most challenging pathogens and most threatening infections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-06T03:48:19Z"
    }
  ]
}
```
