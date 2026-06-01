# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5483?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5483
- Title: Chloe Cole Act
- Congress: 119
- Bill type: HR
- Bill number: 5483
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-03-31T08:05:28Z
- Update date including text: 2026-03-31T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5483",
    "number": "5483",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "O000177",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Onder, Robert F. [R-MO-3]",
        "lastName": "Onder",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Chloe Cole Act",
    "type": "HR",
    "updateDate": "2026-03-31T08:05:28Z",
    "updateDateIncludingText": "2026-03-31T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:04:15Z",
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "NC"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TN"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AL"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "IN"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TN"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WV"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "OH"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "ID"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "SC"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MD"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "NC"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TN"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
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
      "sponsorshipDate": "2025-09-19",
      "state": "IN"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "OK"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "WI"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "WY"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "IL"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "GA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "TX"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "OH"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "VA"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "TX"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "KY"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "NC"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "TX"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "VA"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "FL"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "GA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "MS"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "AL"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NC"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-03-30",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5483ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5483\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Onder (for himself, Mr. Carter of Georgia , Mr. Murphy , Mr. McCormick , Mr. Fleischmann , Mr. Weber of Texas , Mr. Moore of Alabama , Mr. Baird , Mr. Gill of Texas , Mr. Rose , Mr. Moore of West Virginia , Mr. Taylor , Mr. Simpson , Mrs. Biggs of South Carolina , Mr. Crenshaw , Mr. Harris of Maryland , Mr. Harrigan , Mr. Aderholt , Mr. Ogles , and Mr. Collins ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit health care professionals, hospitals, or clinics from participating in the chemical or surgical mutilation of a child and to provide a private right of action for children and the parents of children whose healthy body parts have been damaged by medical professionals practicing chemical and surgical mutilation.\n#### 1. Short title\nThis Act may be cited as the Chloe Cole Act .\n#### 2. Definitions\nIn this Act:\n**(1) Chemical or surgical mutilation**\n**(A) In general**\nThe term chemical or surgical mutilation means engaging in any one or more of the following for the purpose of intentionally halting the natural development of the individual\u2019s body so that it no longer corresponds to the individual\u2019s sex or intentionally changing the individual\u2019s body, including the individual\u2019s external appearance or biological functions, to no longer correspond to the individual\u2019s sex:\n**(i)**\nThe use of puberty blockers, including gonadotropin releasing hormone agonists and other interventions, to delay the onset or progression of normally timed puberty in an individual.\n**(ii)**\nThe use of sex hormones, such as androgen blockers, estrogen, progesterone, or testosterone.\n**(iii)**\nSurgical procedures that attempt to transform an individual's physical appearance or that attempt to alter or remove an individual's sexual organs.\n**(B) Exclusions**\nSuch term does not include any of the following:\n**(i)**\nAppropriate and medically necessary procedures to treat a verifiable disorder of sexual development, including an individual born with 46 XX chromosomes with virilization, with 46 XY chromosomes with undervirilization, or having both ovarian and testicular tissue.\n**(ii)**\nThe treatment of any infection, injury, disease, or disorder that has been caused or exacerbated by the performance of an intervention described in subparagraph (A) without regard to whether the intervention was performed in accordance with State or Federal law or whether the intervention is covered by the private right of action under section 4.\n**(iii)**\nAny intervention undertaken because the individual suffers from any diagnosed and verifiable condition of the body\u2019s organ systems, including the following:\n**(I)**\nTraumatic bodily injuries (such as fractures, organ rupture, or penetrating trauma).\n**(II)**\nCongenital structural anomalies of major organs or systems, including the cardiovascular, respiratory, renal, hepatic, neurological, or musculoskeletal systems.\n**(III)**\nAcute illnesses with a high probability of rapid mortality.\n**(iv)**\nDetransition treatment.\n**(2) Child**\nThe term child means an individual under 18 years of age.\n**(3) Detransition treatment**\nThe term detransition treatment means any treatment, including a mental health treatment, medical intervention, or surgery, that does either or both of the following:\n**(A)**\nStops or reverses the effects of a prior chemical or surgical mutilation.\n**(B)**\nHelps an individual cope with the effects of a prior chemical or surgical mutilation.\n**(4) Health care professional**\nThe term health care professional means a person, including a physician, who is licensed, certified, or otherwise authorized by the laws of a State to administer health care in the ordinary course of the practice of his or her profession or performing such acts which require such licensure.\n**(5) Mental health professional**\nThe term mental health professional means a person who is licensed to diagnose and treat mental health conditions in a State.\n**(6) Participate**\nThe term participate , with respect to acts constituting chemical or surgical mutilation as defined in paragraph (1), means directly engaging in the planning, authorization, prescription, administration, or performance of any such act, including any of the following:\n**(A)**\nPrescribing puberty blockers, sex hormones, or related medications with the intent to alter an individual\u2019s physical appearance or reproductive function to align with an identity differing from his or her sex.\n**(B)**\nAdministering medications or treatments described in subparagraph (A) with such intent, whether by injection, oral delivery, or other means.\n**(C)**\nPerforming surgical procedures that attempt to transform an individual\u2019s physical appearance to confirm a patient\u2019s physical appearance to be of the alternate sex, or that alter or remove sexual organs as part of chemical or surgical mutilation.\n**(D)**\nAuthorizing or directing such chemical or surgical mutilation procedures as a supervising health care professional or institutional representative.\n**(E)**\nKnowingly planning or coordinating the provision of treatments or procedures described above in subparagraph (A), (C), or (D) with the intent to facilitate chemical or surgical mutilation.\n**(7) Sex**\nThe term sex means a person's immutable biological classification, determined at the moment of conception, as either male or female, as follows:\n**(A)**\nThe term female is a person who naturally has, had, will have, or would have but for a congenital anomaly or intentional or unintentional disruption, the reproductive system that produces, transports, and utilizes the large gamete (ova) for fertilization.\n**(B)**\nThe term male is a person who naturally has, had, will have, or would have but for a congenital anomaly or intentional or unintentional disruption, the reproductive system that produces, transports, and utilizes the small gamete (sperm) for fertilization.\n#### 3. Prohibition on chemical or surgical mutilation\n##### (a) In general\nNo health care professional, hospital, or clinic shall, in a circumstance described in subsection (b), participate in the chemical or surgical mutilation of a child, and a health care professional, hospital, or clinic may commence participation in a treatment that qualifies as an exception specified in clauses (i) through (iv) of section 2(1)(B) only after determining that clear and convincing evidence supports a determination that the treatment so qualifies.\n##### (b) Circumstances described\nThe circumstances described in this subsection are that\u2014\n**(1)**\nthe defendant or child traveled in interstate or foreign commerce, or traveled using a means, channel, facility, or instrumentality of interstate or foreign commerce, in furtherance of or in connection with the participation in the chemical or surgical mutilation;\n**(2)**\nthe defendant used a means, channel, facility, or instrumentality of interstate or foreign commerce in furtherance of or in connection with the participation in the chemical or surgical mutilation;\n**(3)**\nany payment of any kind was made, directly or indirectly, in furtherance of or in connection with the participation in the chemical or surgical mutilation using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate or foreign commerce;\n**(4)**\nthe defendant transmitted in interstate or foreign commerce any communication relating to or in furtherance of the participation in the chemical or surgical mutilation using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate or foreign commerce by any means or in any manner, including by computer, mail, wire, or electromagnetic transmission;\n**(5)**\nany instrument, item, substance, or other object that has traveled in interstate or foreign commerce was used to perform the chemical or surgical mutilation;\n**(6)**\nthe chemical or surgical mutilation occurred within the District of Columbia, the special maritime and territorial jurisdiction of the United States, or any territory or possession of the United States; or\n**(7)**\nthe chemical or surgical mutilation otherwise occurred in or affected interstate or foreign commerce.\n#### 4. Private right of action\n##### (a) In general\nAn individual subjected as a child to chemical or surgical mutilation prohibited by section 3, or the parents or legal guardians of such individual, may bring a civil action in an appropriate district court of the United States for damages against any health care professional, hospital, or clinic, who participates in the chemical or surgical mutilation of that child. Such a cause of action shall be available regardless of whether the alleged chemical or surgical mutilation occurred before, on, or after the date of enactment of this Act.\n##### (b) Damages\nDamages available pursuant to such an action may include\u2014\n**(1)**\ncompensatory damages, including all economic damages associated with undoing, correcting, or ameliorating the effects or results of any chemical or surgical mutilation procedures;\n**(2)**\nnon-economic damages for emotional distress and pain and suffering; and\n**(3)**\npunitive damages, if the claimant proves by clear and convincing evidence that the defendant against whom punitive damages are sought acted maliciously, intentionally, fraudulently, or recklessly.\n##### (c) Strict liability\nAny health care professional, hospital, or clinic whose participation in the chemical or surgical mutilation of a child after the date of enactment of this Act is proven by clear and convincing evidence shall be strictly liable for damages for any such act of mutilation. If a treatment qualifies under an exception specified in clauses (i) through (iv) of section 2(1)(B), and that is raised as an affirmative defense to a violation of this Act, the health care professional, hospital, or clinic shall bear the burden of proving by clear and convincing evidence that such exception applies.\n#### 5. Rules of construction\nIn this Act:\n**(1)**\nNo private right of action is established based on counseling, referrals to mental health professionals, or discussions of treatment options, including counseling, referrals, or options available upon reaching adulthood, or in circumstances not described in section 3(b), provided by health care professionals, or mental health professionals, provided that such actions do not constitute participation in chemical or surgical mutilation, as defined in section 2.\n**(2)**\nNo liability for a health care professional under these provisions may be waived.\n**(3)**\nAny ambiguities shall be resolved against any party found to have engaged in participation, as defined in section 2(6), in the chemical or surgical mutilation of a child.\n**(4)**\nIn any cases in which chemical or surgical mutilation of a child is shown to have occurred before the date of enactment of this Act, there is limited deference to prevailing standards of care to the extent that such standards contradict the intent of this Act and it is shown that the health care professional knew or should have known that such standards of care were in serious, scientific, and medical dispute at the time of the chemical or surgical mutilation.\n**(5)**\nNothing in this Act shall be construed to prohibit a health care professional or mental health professional from providing information about all available treatment options, discussing risks and benefits, or expressing professional medical opinions, so long as such actions do not constitute participation in chemical or surgical mutilation.\n#### 6. Statute of limitations\nAn action under section 4 may be brought within 25 years from the date of the eighteenth birthday of an individual subjected to chemical or surgical mutilation as a child or within 4 years from the time the cost of a detransition treatment is incurred, whichever date is later.\n#### 7. Severability\nIf any provision of this Act, or the application of such a provision to any person or circumstance, is held to be unconstitutional, the remainder of this Act, and the application of the provision held to be unconstitutional to any other person or circumstance, shall not be affected.",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-09-18",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2907",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Chloe Cole Act",
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
        "name": "Health",
        "updateDate": "2025-11-18T16:16:08Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5483ih.xml"
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
      "title": "Chloe Cole Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T04:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chloe Cole Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit health care professionals, hospitals, or clinics from participating in the chemical or surgical mutilation of a child and to provide a private right of action for children and the parents of children whose healthy body parts have been damaged by medical professionals practicing chemical and surgical mutilation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T04:48:17Z"
    }
  ]
}
```
