# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2226?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2226
- Title: Let Pregnancy Centers Serve Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2226
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-12-03T09:06:27Z
- Update date including text: 2025-12-03T09:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2226",
    "number": "2226",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S000522",
        "district": "4",
        "firstName": "Christopher",
        "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
        "lastName": "Smith",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Let Pregnancy Centers Serve Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-03T09:06:27Z",
    "updateDateIncludingText": "2025-12-03T09:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:06:10Z",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-18",
      "state": "AL"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "ID"
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
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "SC"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "MN"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MS"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MD"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "NJ"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "MO"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "WI"
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
      "sponsorshipDate": "2025-06-11",
      "state": "VA"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "CO"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2226ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2226\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Smith of New Jersey (for himself, Ms. Tenney , and Mr. Aderholt ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to prohibit discrimination against entities that do not participate in abortion and to strengthen implementation and enforcement of Federal conscience laws.\n#### 1. Short title\nThis Act may be cited as the Let Pregnancy Centers Serve Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nPregnancy centers are community-based, nonprofit organizations that provide free compassionate care, support, and resources to help meet the physical, psychological, emotional, and spiritual needs of women, girls, couples, and families navigating pregnancy and offer life-affirming alternatives to abortion. These services can include pregnancy tests, ultrasounds, STD/STI tests, prenatal education programs, parenting education programs, after-abortion support, lactation consultations, certified dietician and nutritionist consultations, and well-women exams.\n**(2)**\nPregnancy care centers are committed to providing clients with complete and accurate information regarding their pregnancy options and the development of an unborn baby. Most pregnancy centers are affiliated with at least one of three national networks. These networks require their affiliates to adopt a Commitment of Care and Competence, setting ethical, legal, and regulatory standards.\n**(3)**\nIn 2022 alone, 2,750 pregnancy centers across the United States provided an estimated 3,255,856 total client sessions, including in-person and virtual sessions. 97.4 percent of clients seen by pregnancy centers reported having a positive experience with pregnancy centers.\n**(4)**\nThe total values of the material goods and services provided by pregnancy centers in 2022 was at least $367 million. 808,737 clients received material resources, which included packs of diapers and wipes, baby formula, baby clothes, new cribs, new car seats, and strollers.\n**(5)**\nOut of the 62,576 individuals who worked at pregnancy centers in 2022, 44,930 (7 in 10 workers) were volunteers.\n**(6)**\nMany pregnancy centers offer medical services. In 2022, 10,175 medical staff and volunteers provided care to clients across the Nation. Pregnancy centers performed 546,683 free ultrasounds, at an estimated total value of $136 million.\n#### 3. Prohibiting discrimination against entities that do not participate in abortion\nTitle II of the Public Health Service Act ( 42 U.S.C. 202 et seq. ) is amended by inserting after section 245 the following:\n245A. Prohibiting discrimination against entities that do not participate in abortion (a) In general Notwithstanding any other law, the Federal Government, and any individual or entity that receives Federal financial assistance, including any State or local government, may not discriminate against, penalize, or retaliate against an entity because the entity offers life-affirming support and resources to women facing unexpected pregnancy, offers life-affirming alternatives to abortion, or refrains from actions that counsel in favor of, suggest, recommend, assist, provide, promote, or in any way participate in the performance of abortions. (b) Prohibited actions The actions that are prohibited under subsection (a) include, at a minimum\u2014 (1) requiring an entity to offer or perform an abortion; (2) requiring an entity to offer, provide, or distribute an abortion-inducing drug; (3) requiring an entity to refer a person for an abortion or an abortion-inducing drug; (4) requiring an entity to counsel in favor of an abortion or an abortion-inducing drug; (5) requiring an entity to post any advertisement, sign, flyer, or similar material that promotes or provides information about obtaining an abortion or an abortion-inducing drug; and (6) prohibiting an entity from providing information, care, counseling, classes, or other services related to pregnancy, childbirth, or parenting because the entity does not perform, refer, or counsel in favor of an abortion or an abortion-inducing drug. (c) Rule of construction Nothing in this section shall be construed\u2014 (1) to prevent any entity from voluntarily electing to participate in abortions or abortion referrals where not prohibited by any other law; or (2) to affect, or be affected by, any Federal law that requires stabilizing treatment for a pregnant woman or her unborn child when either needs emergency care. (d) Definitions For purposes of this section: (1) Abortion The term abortion means the use or prescription of any instrument, medicine, drug, or any other substance or device\u2014 (A) to intentionally kill the unborn child of a woman known to be pregnant; or (B) to intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) after viability to produce a live birth and preserve the life and health of the child born alive; (ii) to remove a dead unborn child; or (iii) to remove an ectopic pregnancy or other pregnancy implanted outside the uterus. (2) Federal financial assistance The term Federal financial assistance means Federal payments to cover the cost of health care services or benefits, or other Federal payments, grants, or loans to promote or otherwise facilitate health-related activities. Such term does not include expenditures made under direct spending programs. (3) Life-affirming alternatives to abortion The term life-affirming alternatives to abortion means one or more programs that promote childbirth as an alternative to abortion, through life-affirming social services providers, which may include pregnancy centers, adoption assistance providers, and maternity homes. For purposes of the preceding sentence, the term life-affirming social services providers does not include entities that provide, facilitate, counsel in favor of, or refer for abortions. (4) Life-affirming support and resources to women facing unexpected pregnancy (A) In general The term life-affirming support and resources to women facing unexpected pregnancy means one or more of the following: (i) Providing information, care, counseling, classes, or other services related to pregnancy, childbirth, or parenting without providing, referring, or counseling in favor of abortion or abortion-inducing drugs. (ii) Providing prenatal and postnatal resources, such as diapers, baby clothes, baby furniture, formula, and similar items. (iii) Providing medical testing, counseling, and care related to pregnancy or childbirth. (iv) Counseling a woman on pregnancy-related care or treatment, including care or treatment that may reverse the effects of abortion-inducing drugs. (B) Limitation The term life-affirming support and resources to women facing unexpected pregnancy does not include performing, referring, or counseling in favor of abortion or abortion-inducing drugs. (5) State or local government The term State or local government includes every agency and other governmental unit and subdivision of a State or local government, if such State or local government, or any agency or governmental unit or subdivision thereof, receives Federal financial assistance. .\n#### 4. Strengthening enforcement of Federal conscience laws\nTitle II of the Public Health Service Act ( 42 U.S.C. 202 et seq. ), as amended by section 3, is further amended by inserting after section 245A the following:\n245B. Civil action for discrimination against entities offering abortion alternatives (a) In general A qualified party may, in a civil action, obtain relief described in subsection (e) with respect to a designated violation. (b) Definitions For purposes of this section: (1) Designated violation The term designated violation means an actual or threatened violation of any provision of law described in section 245A. (2) Qualified party The term qualified party means\u2014 (A) the Attorney General; or (B) any individual or entity adversely affected by the designated violation. (c) Administrative remedies not required An action under this section may be commenced, and relief may be granted, without regard to whether the party commencing the action has sought or exhausted any available administrative remedies. (d) Defendants in actions under this section may include governmental entities as well as others (1) In general An action under this section may be maintained against any individual or entity receiving Federal financial assistance (as defined in section 245A(c)), including a State governmental entity. Relief in an action under this section may include money damages even if the defendant is a governmental entity. (2) Definition For the purposes of this subsection, the term State governmental entity means a State, a local government within a State, and any agency or other governmental unit or subdivision of a State, or of such a local government. (e) Nature of relief In an action under this section, the court shall grant\u2014 (1) all appropriate relief, including injunctive relief, declaratory relief, and compensatory damages to prevent the occurrence, continuance, or repetition of the designated violation and to compensate for losses resulting from the designated violation; and (2) to a prevailing plaintiff, reasonable attorneys\u2019 fees and litigation costs. .\n#### 5. Severability\nIf any provision of this Act or an amendment made by this Act, or the application of such a provision or amendment to any individual, entity, government, or circumstance, is held to be unconstitutional, the remainder of this Act and the amendments made by this Act, and the application of such provision or amendment to any other individual, entity, government, or circumstance, shall not be affected.",
      "versionDate": "2025-03-18",
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
        "updateDate": "2025-04-04T16:20:26Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2226ih.xml"
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
      "title": "Let Pregnancy Centers Serve Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Let Pregnancy Centers Serve Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to prohibit discrimination against entities that do not participate in abortion and to strengthen implementation and enforcement of Federal conscience laws.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:24Z"
    }
  ]
}
```
