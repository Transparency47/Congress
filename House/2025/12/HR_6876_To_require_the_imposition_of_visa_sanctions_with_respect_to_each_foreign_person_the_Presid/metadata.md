# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6876?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6876
- Title: Protecting Children from Foreign Mutilation Act
- Congress: 119
- Bill type: HR
- Bill number: 6876
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-03-13T08:05:41Z
- Update date including text: 2026-03-13T08:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6876",
    "number": "6876",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001240",
        "district": "6",
        "firstName": "Addison",
        "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
        "lastName": "McDowell",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Protecting Children from Foreign Mutilation Act",
    "type": "HR",
    "updateDate": "2026-03-13T08:05:41Z",
    "updateDateIncludingText": "2026-03-13T08:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "OK"
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
      "sponsorshipDate": "2025-12-18",
      "state": "TX"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "IN"
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
      "sponsorshipDate": "2025-12-18",
      "state": "OH"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NC"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "AZ"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "IL"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TN"
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
      "sponsorshipDate": "2026-01-09",
      "state": "OH"
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
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6876ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6876\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. McDowell (for himself, Mr. Brecheen , Mr. Weber of Texas , Mr. Stutzman , Mr. Taylor , Mr. Moore of North Carolina , and Mr. Hamadeh of Arizona ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the imposition of visa sanctions with respect to each foreign person the President determines has performed or otherwise facilitated chemical or surgical mutilations of United States minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Children from Foreign Mutilation Act .\n#### 2. Imposition of sanctions\n##### (a) In general\nThe President shall impose the sanction described in subsection (b) with respect to each person the President determines, including through information submitted in accordance with subsection (d), is a foreign person who\u2014\n**(1)**\nis a member of the World Professional Association for Transgender Health;\n**(2)**\nhas, in the capacity of such individual as a duly licensed physician, in any way performed, prescribed, or otherwise facilitated chemical or surgical mutilations of United States persons; or\n**(3)**\nowns or operates a clinic, hospital, pharmacy, or other medical institution that performs, prescribes, or otherwise facilitates chemical or surgical mutilations of United States persons.\n##### (b) Visa sanctions\nThe sanction described in this subsection is the following:\n**(1) Visas, admission, or parole**\nA foreign person described in subsection (a) is\u2014\n**(A)**\ninadmissible to the United States;\n**(B)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(C)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(2) Current visas revoked**\n**(A) In general**\nA foreign person described in subsection (a) shall be subject to revocation of any visa or other entry documentation regardless of when the visa or other entry documentation is or was issued.\n**(B) Immediate effect**\nA revocation under subparagraph (A) shall take effect immediately and automatically cancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n##### (c) Information submitted to Secretary of State\nThe Secretary of State shall establish procedures to enable individuals to submit to the Secretary information relating to foreign persons that may qualify for the imposition of sanctions under this Act.\n##### (d) Exception; waiver\n**(1) Exception to comply with international obligations**\nSanctions under this section shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with\u2014\n**(A)**\nthe Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States; or\n**(B)**\nother applicable international obligations.\n**(2) Exception with respect to whistleblowers**\nSanctions under this section shall not be imposed with respect to a foreign person described in subsection (a)(2) if the Secretary of State determines that such foreign person\u2014\n**(A)**\nno longer works for an entity performing any of the acts described in subsection (c); and\n**(B)**\n**(i)**\nhas provided information to the Secretary of State sufficient to identify at least one other foreign person meeting the criteria for the imposition of sanctions under this section; or\n**(ii)**\nhas provided information to any other Federal official relating to a violation of law or regulation in the practices of the entity described in subparagraph (A).\n**(3) Waiver**\nThe President may waive the application of sanctions under this section with respect to a foreign person if the President determines that such a waiver is in the national security interests of the United States.\n##### (e) Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall submit to Congress a report that includes\u2014\n**(1)**\na description of the actions taken to carry out this Act;\n**(2)**\nthe number of people who have been sanctioned pursuant to the authorities provided by this Act; and\n**(3)**\nany additional measures the Secretary would recommend to be taken to discourage foreign persons from providing gender transitions to United States persons.\n##### (f) Definitions\nIn this section:\n**(1) Admission; admitted; alien**\nThe terms admission , admitted , and alien have the meanings given such terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Chemical or surgical mutilation**\n**(A) In general**\nThe term chemical or surgical mutilation means engaging in any one or more of the following for the purpose of intentionally halting the natural development of the individual\u2019s body so that it no longer corresponds to the individual\u2019s sex or intentionally changing the individual\u2019s body, including the individual\u2019s external appearance or biological functions, to no longer correspond to the individual\u2019s sex:\n**(i)**\nThe use of puberty blockers, including gonadotropin releasing hormone agonists and other interventions, to delay the onset or progression of normally timed puberty in an individual.\n**(ii)**\nThe use of sex hormones, such as androgen blockers, estrogen, progesterone, or testosterone.\n**(iii)**\nSurgical procedures that attempt to transform an individual\u2019s physical appearance or that attempt to alter or remove an individual\u2019s sexual organs.\n**(B) Exclusions**\nSuch term does not include any of the following:\n**(i)**\nAppropriate and medically necessary procedures to treat a verifiable disorder of sexual development, including an individual born with 46 XX chromosomes with virilization, with 46 XY chromosomes with undervirilization, or having both ovarian and testicular tissue.\n**(ii)**\nThe treatment of any infection, injury, disease, or disorder that has been caused or exacerbated by the performance of an intervention described in subparagraph (A) without regard to whether the intervention was performed in accordance with State or Federal law or whether the intervention is covered by the private right of action under section 4.\n**(iii)**\nAny intervention undertaken because the individual suffers from any diagnosed and verifiable condition of the body\u2019s organ systems, including the following:\n**(I)**\nTraumatic bodily injuries (such as fractures, organ rupture, or penetrating trauma).\n**(II)**\nCongenital structural anomalies of major organs or systems, including the cardiovascular, respiratory, renal, hepatic, neurological, or musculoskeletal systems.\n**(III)**\nAcute illnesses with a high probability of rapid mortality.\n**(iv)**\nDetransition treatment.\n**(3) Detransition treatment**\nThe term detransition treatment means any treatment, including a mental health treatment, medical intervention, or surgery, that does either or both of the following:\n**(A)**\nStops or reverses the effects of a prior chemical or surgical mutilation.\n**(B)**\nHelps an individual cope with the effects of a prior chemical or surgical mutilation.\n**(4) Foreign person**\nThe term foreign person means an individual who is not a citizen or national of the United States.\n**(5) Sex**\nThe term sex means a person\u2019s immutable biological classification, determined at the moment of conception, as either male or female.\n**(6) United States person**\nThe term United States person means an individual who\u2014\n**(A)**\nis a United States citizen or national, or an alien lawfully admitted for permanent residence to the United States; and\n**(B)**\nhas not attained the age of 18 years.\n#### 3. Severability\nIf any provision of this Act or the application of such provision to any person, entity, government, or circumstance, is held to be unconstitutional, the remainder of this Act, or the application of such provision to all other persons, entities, governments, or circumstances, shall not be affected thereby.",
      "versionDate": "2025-12-18",
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
        "name": "Immigration",
        "updateDate": "2026-01-26T13:41:11Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6876ih.xml"
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
      "title": "Protecting Children from Foreign Mutilation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T03:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Children from Foreign Mutilation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the imposition of visa sanctions with respect to each foreign person the President determines has performed or otherwise facilitated chemical or surgical mutilations of United States minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T03:33:20Z"
    }
  ]
}
```
