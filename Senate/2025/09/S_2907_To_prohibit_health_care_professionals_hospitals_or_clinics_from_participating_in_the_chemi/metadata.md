# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2907?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2907
- Title: Chloe Cole Act
- Congress: 119
- Bill type: S
- Bill number: 2907
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-05-19T11:03:44Z
- Update date including text: 2026-05-19T11:03:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2907",
    "number": "2907",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Chloe Cole Act",
    "type": "S",
    "updateDate": "2026-05-19T11:03:44Z",
    "updateDateIncludingText": "2026-05-19T11:03:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
        "item": [
          {
            "date": "2025-09-18T21:55:12Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-18T21:55:12Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MO"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "FL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "TX"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "NC"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "FL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "AL"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "UT"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "IN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "MS"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "OK"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2907is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2907\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mrs. Blackburn (for herself, Mr. Schmitt , Mr. Sheehy , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit health care professionals, hospitals, or clinics from participating in the chemical or surgical mutilation of a child and to provide a private right of action for children and the parents of children whose healthy body parts have been damaged by medical professionals practicing chemical and surgical mutilation.\n#### 1. Short title\nThis Act may be cited as the Chloe Cole Act .\n#### 2. Definitions\nIn this Act:\n**(1) Chemical or surgical mutilation**\n**(A) In general**\nThe term chemical or surgical mutilation means engaging in any one or more of the following for the purpose of intentionally halting the natural development of the individual\u2019s body so that it no longer corresponds to the individual\u2019s sex or intentionally changing the individual\u2019s body, including the individual\u2019s external appearance or biological functions, to no longer correspond to the individual\u2019s sex:\n**(i)**\nThe use of puberty blockers, including gonadotropin releasing hormone agonists and other interventions, to delay the onset or progression of normally timed puberty in an individual.\n**(ii)**\nThe use of sex hormones, such as androgen blockers, estrogen, progesterone, or testosterone.\n**(iii)**\nSurgical procedures that attempt to transform an individual's physical appearance or that attempt to alter or remove an individual's sexual organs.\n**(B) Exclusions**\nSuch term does not include any of the following:\n**(i)**\nAppropriate and medically necessary procedures to treat a verifiable disorder of sexual development, including an individual born with 46 XX chromosomes with virilization, with 46 XY chromosomes with undervirilization, or having both ovarian and testicular tissue.\n**(ii)**\nThe treatment of any infection, injury, disease, or disorder that has been caused or exacerbated by the performance of an intervention described in subparagraph (A) without regard to whether the intervention was performed in accordance with State or Federal law or whether the intervention is covered by the private right of action under section 4.\n**(iii)**\nAny intervention undertaken because the individual suffers from any diagnosed and verifiable condition of the body\u2019s organ systems, including the following:\n**(I)**\nTraumatic bodily injuries (such as fractures, organ rupture, or penetrating trauma).\n**(II)**\nCongenital structural anomalies of major organs or systems, including the cardiovascular, respiratory, renal, hepatic, neurological, or musculoskeletal systems.\n**(III)**\nAcute illnesses with a high probability of rapid mortality.\n**(iv)**\nDetransition treatment.\n**(2) Child**\nThe term child means an individual under 18 years of age.\n**(3) Detransition treatment**\nThe term detransition treatment means any treatment, including a mental health treatment, medical intervention, or surgery, that does either or both of the following:\n**(A)**\nStops or reverses the effects of a prior chemical or surgical mutilation.\n**(B)**\nHelps an individual cope with the effects of a prior chemical or surgical mutilation.\n**(4) Health care professional**\nThe term health care professional means a person, including a physician, who is licensed, certified, or otherwise authorized by the laws of a State to administer health care in the ordinary course of the practice of his or her profession or performing such acts which require such licensure.\n**(5) Mental health professional**\nThe term mental health professional means a person who is licensed to diagnose and treat mental health conditions in a State.\n**(6) Participate**\nThe term participate , with respect to acts constituting chemical or surgical mutilation as defined in paragraph (1), means directly engaging in the planning, authorization, prescription, administration, or performance of any such act, including any of the following:\n**(A)**\nPrescribing puberty blockers, sex hormones, or related medications with the intent to alter an individual\u2019s physical appearance or reproductive function to align with an identity differing from his or her sex.\n**(B)**\nAdministering medications or treatments described in subparagraph (A) with such intent, whether by injection, oral delivery, or other means.\n**(C)**\nPerforming surgical procedures that attempt to transform an individual\u2019s physical appearance to confirm a patient\u2019s physical appearance to be of the alternate sex, or that alter or remove sexual organs as part of chemical or surgical mutilation.\n**(D)**\nAuthorizing or directing such chemical or surgical mutilation procedures as a supervising health care professional or institutional representative.\n**(E)**\nKnowingly planning or coordinating the provision of treatments or procedures described above in subparagraph (A), (C), or (D) with the intent to facilitate chemical or surgical mutilation.\n**(7) Sex**\nThe term sex means a person's immutable biological classification, determined at the moment of conception, as either male or female, as follows:\n**(A)**\nThe term female is a person who naturally has, had, will have, or would have but for a congenital anomaly or intentional or unintentional disruption, the reproductive system that produces, transports, and utilizes the large gamete (ova) for fertilization.\n**(B)**\nThe term male is a person who naturally has, had, will have, or would have but for a congenital anomaly or intentional or unintentional disruption, the reproductive system that produces, transports, and utilizes the small gamete (sperm) for fertilization.\n#### 3. Prohibition on chemical or surgical mutilation\n##### (a) In general\nNo health care professional, hospital, or clinic shall, in a circumstance described in subsection (b), participate in the chemical or surgical mutilation of a child, and a health care professional, hospital, or clinic may commence participation in a treatment that qualifies as an exception specified in clauses (i) through (iv) of section 2(1)(B) only after determining that clear and convincing evidence supports a determination that the treatment so qualifies.\n##### (b) Circumstances described\nThe circumstances described in this subsection are that\u2014\n**(1)**\nthe defendant or child traveled in interstate or foreign commerce, or traveled using a means, channel, facility, or instrumentality of interstate or foreign commerce, in furtherance of or in connection with the participation in the chemical or surgical mutilation;\n**(2)**\nthe defendant used a means, channel, facility, or instrumentality of interstate or foreign commerce in furtherance of or in connection with the participation in the chemical or surgical mutilation;\n**(3)**\nany payment of any kind was made, directly or indirectly, in furtherance of or in connection with the participation in the chemical or surgical mutilation using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate or foreign commerce;\n**(4)**\nthe defendant transmitted in interstate or foreign commerce any communication relating to or in furtherance of the participation in the chemical or surgical mutilation using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate or foreign commerce by any means or in any manner, including by computer, mail, wire, or electromagnetic transmission;\n**(5)**\nany instrument, item, substance, or other object that has traveled in interstate or foreign commerce was used to perform the chemical or surgical mutilation;\n**(6)**\nthe chemical or surgical mutilation occurred within the District of Columbia, the special maritime and territorial jurisdiction of the United States, or any territory or possession of the United States; or\n**(7)**\nthe chemical or surgical mutilation otherwise occurred in or affected interstate or foreign commerce.\n#### 4. Private right of action\n##### (a) In general\nAn individual subjected as a child to chemical or surgical mutilation prohibited by section 3, or the parents or legal guardians of such individual, may bring a civil action in an appropriate district court of the United States for damages against any health care professional, hospital, or clinic, who participates in the chemical or surgical mutilation of that child. Such a cause of action shall be available regardless of whether the alleged chemical or surgical mutilation occurred before, on, or after the date of enactment of this Act.\n##### (b) Damages\nDamages available pursuant to such an action may include\u2014\n**(1)**\ncompensatory damages, including all economic damages associated with undoing, correcting, or ameliorating the effects or results of any chemical or surgical mutilation procedures;\n**(2)**\nnon-economic damages for emotional distress and pain and suffering; and\n**(3)**\npunitive damages, if the claimant proves by clear and convincing evidence that the defendant against whom punitive damages are sought acted maliciously, intentionally, fraudulently, or recklessly.\n##### (c) Strict liability\nAny health care professional, hospital, or clinic whose participation in the chemical or surgical mutilation of a child after the date of enactment of this Act is proven by clear and convincing evidence shall be strictly liable for damages for any such act of mutilation. If a treatment qualifies under an exception specified in clauses (i) through (iv) of section 2(1)(B), and that is raised as an affirmative defense to a violation of this Act, the health care professional, hospital, or clinic shall bear the burden of proving by clear and convincing evidence that such exception applies.\n#### 5. Rules of construction\nIn this Act:\n**(1)**\nNo private right of action is established based on counseling, referrals to mental health professionals, or discussions of treatment options, including counseling, referrals, or options available upon reaching adulthood, or in circumstances not described in section 3(b), provided by health care professionals, or mental health professionals, provided that such actions do not constitute participation in chemical or surgical mutilation, as defined in section 2.\n**(2)**\nNo liability for a health care professional under these provisions may be waived.\n**(3)**\nAny ambiguities shall be resolved against any party found to have engaged in participation, as defined in section 2(6), in the chemical or surgical mutilation of a child.\n**(4)**\nIn any cases in which chemical or surgical mutilation of a child is shown to have occurred before the date of enactment of this Act, there is limited deference to prevailing standards of care to the extent that such standards contradict the intent of this Act and it is shown that the health care professional knew or should have known that such standards of care were in serious, scientific, and medical dispute at the time of the chemical or surgical mutilation.\n**(5)**\nNothing in this Act shall be construed to prohibit a health care professional or mental health professional from providing information about all available treatment options, discussing risks and benefits, or expressing professional medical opinions, so long as such actions do not constitute participation in chemical or surgical mutilation.\n#### 6. Statute of limitations\nAn action under section 4 may be brought within 25 years from the date of the eighteenth birthday of an individual subjected to chemical or surgical mutilation as a child or within 4 years from the time the cost of a detransition treatment is incurred, whichever date is later.\n#### 7. Severability\nIf any provision of this Act, or the application of such a provision to any person or circumstance, is held to be unconstitutional, the remainder of this Act, and the application of the provision held to be unconstitutional to any other person or circumstance, shall not be affected.",
      "versionDate": "2025-09-18",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "5483",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Chloe Cole Act",
      "type": "HR"
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
        "updateDate": "2025-11-18T16:16:40Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2907is.xml"
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
      "title": "Chloe Cole Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T11:03:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chloe Cole Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit health care professionals, hospitals, or clinics from participating in the chemical or surgical mutilation of a child and to provide a private right of action for children and the parents of children whose healthy body parts have been damaged by medical professionals practicing chemical and surgical mutilation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T05:48:19Z"
    }
  ]
}
```
