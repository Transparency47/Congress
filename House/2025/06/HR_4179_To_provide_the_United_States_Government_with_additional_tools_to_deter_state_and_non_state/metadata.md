# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4179?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4179
- Title: Countering Wrongful Detention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4179
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2025-10-18T08:05:52Z
- Update date including text: 2025-10-18T08:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4179",
    "number": "4179",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001072",
        "district": "2",
        "firstName": "J.",
        "fullName": "Rep. Hill, J. French [R-AR-2]",
        "lastName": "Hill",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Countering Wrongful Detention Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-18T08:05:52Z",
    "updateDateIncludingText": "2025-10-18T08:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-26T14:06:30Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "NJ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "NY"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "VA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "GA"
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
      "sponsorshipDate": "2025-10-17",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4179ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4179\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Hill of Arkansas (for himself, Mr. Kean , Mr. Lawler , Mr. Moskowitz , and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide the United States Government with additional tools to deter state and non-state actors from wrongfully detaining United States nationals for political leverage, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Countering Wrongful Detention Act of 2025 .\n#### 2. Designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention\nThe Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741 et seq. ) is amended by inserting after section 306 the following:\n306A. Designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention (a) In general Subject to the notice requirement of subsection (d)(1)(A), the Secretary of State, in consultation with the heads of other relevant Federal agencies, may designate a foreign country that has provided support for or directly engaged in the unlawful or wrongful detention of a United States national as a State Sponsor of Unlawful or Wrongful Detention based on any of the following criteria: (1) The unlawful or wrongful detention of a United States national occurs in the foreign country. (2) The government of the foreign country or a nonstate actor in the foreign country has failed to release an unlawfully or wrongfully detained United States national within 30 days of being notified by the Department of State of such unlawfully or wrongfully detained national. (3) Actions taken by the government of the foreign country indicate that the government is responsible for, complicit in, or materially supports the unlawful or wrongful detention of a United States national, including by acting as described in paragraph (2) after having been notified by the Department of State. (4) The actions of a state or nonstate actor in the foreign country, including any previous action relating to unlawful or wrongful detention or hostage taking of a United States national, pose a risk to the safety and security of United States nationals abroad sufficient to warrant designation of the foreign country as a State Sponsor of Unlawful or Wrongful Detention, as determined by the Secretary. (b) Termination of designation (1) Termination by the Secretary of State The Secretary of State may terminate the designation of a foreign country under subsection (a) if the Secretary certifies to Congress that it is in the national interest to terminate such designation and that the foreign country\u2014 (A) has released the United States nationals unlawfully or wrongfully detained within the territory of the foreign country; (B) has demonstrated changes in policies with respect to unlawful or wrongful detention and hostage taking; or (C) has provided assurances that the government of the foreign country will not engage or be complicit in or support acts described in subsection (a). (2) Termination unless approval by Congress The designation of a foreign country under subsection (a) shall terminate on the date that is 6 months after such designation unless a joint resolution of approval with respect to the designation is enacted into law. (c) Prohibition on subsequent designations if designation not approved; exception (1) In general If a joint resolution of approval is not enacted into law with respect to a designation of a foreign country under subsection (a) before the expiration of the 6-month period described in subsection (b)(2), the Secretary of State may not designate the foreign country under subsection (a) during the 6-month period beginning on the date of the expiration of the 6-month period described in subsection (b)(2). (2) Exception A foreign country with respect to which a designation under subsection (a) has terminated by reason of the application of subsection (b)(2) may be re-designated as a State Sponsor of Unlawful or Wrongful Detention for purposes of subsection (a) if a joint resolution providing for such designation is enacted into law. (d) Briefing and reports to Congress; publication (1) Reports to Congress (A) In general Not later than 7 days after making a designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention under subsection (a), the Secretary of State shall submit to the appropriate congressional committees a report that notifies the committees of the proposed designation. (B) Elements In each report submitted under subparagraph (A) with respect to the designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention, the Secretary shall include\u2014 (i) the justification for the designation; and (ii) a description of any action taken by the United States Government, including the Secretary of State or the head of any other relevant Federal agency, to deter the unlawful or wrongful detention of foreign nationals in the country. (2) Initial briefing required Not later than 60 days after the date of the enactment of this section, the Secretary shall brief the appropriate congressional committees on the following: (A) Whether any of the following countries should be designated as a State Sponsor of Unlawful or Wrongful Detention under subsection (a): (i) Afghanistan. (ii) Eritrea. (iii) The Islamic Republic of Iran. (iv) Nicaragua. (v) The Russian Federation. (vi) The Syrian Arab Republic. (vii) Venezuela under the regime of Nicol\u00e1s Maduro. (viii) The Republic of Belarus. (ix) The People\u2019s Republic of China. (B) The steps taken by the Secretary to deter the unlawful and wrongful detention of United States nationals and to respond to such detentions, including\u2014 (i) any engagement with private sector companies to optimize the distribution of travel advisories; and (ii) any engagement with private companies responsible for promoting travel to foreign countries engaged in the unlawful or wrongful detention of United States nationals. (C) An assessment of a possible expansion of chapter 97 of title 28, United States Code (commonly known as the Foreign Sovereign Immunities Act of 1976 ) to include an exception from asset seizure immunity for State Sponsors of Unlawful or Wrongful Detention. (D) The progress made in multilateral fora, including the United Nations and other international organizations, to address the unlawful and wrongful detention of United States nationals, in addition to nationals of partners and allies of the United States in foreign countries. (3) Annual briefing Not later than one year after the date of the enactment of this section, and annually thereafter for 5 years, the Assistant Secretary of State for Consular Affairs and the Special Presidential Envoy for Hostage Affairs, or designees thereof, shall provide a briefing to the appropriate congressional committees on the countries listed under paragraph (2)(A) and actions taken by the Secretary of State to deter the wrongful detention of United States nationals, including any steps taken in accordance with paragraph (2)(B). (4) Testimony The Special Presidential Envoy for Hostage Affairs shall testify before the appropriate congressional committees not less than once each Congress on activities to deter wrongful detention. (5) Publication The Secretary shall make available on a publicly accessible website of the Department of State, and regularly update, a list of foreign countries designated as State Sponsors of Unlawful or Wrongful Detention under subsection (a). (6) Appropriate committees of congress defined In this subsection, the term appropriate congressional committees means\u2014 (A) the Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives; and (B) the Committee on Foreign Relations and the Committee on Appropriations of the Senate. (e) Review and determination of available responses to state sponsors of unlawful or wrongful detention Upon designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention under subsection (a), the Secretary of State, in consultation with the heads of other relevant Federal agencies, shall conduct a comprehensive review and make a determination of the use of existing authorities to respond to and deter the unlawful or wrongful detention of United States nationals in the foreign country, including\u2014 (1) inadmissibilities available under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ); (2) visa restrictions available under section 7031(c) of the Department of State, Foreign Operations, and Related Programs Appropriations Act, 2024 (division F of Public Law 118\u201347 ; 8 U.S.C. 1182 note) or any other provision of Federal law; (3) sanctions available under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ); (4) restrictions on assistance provided to the government of the country under the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) or any other provision of Federal law; (5) restrictions on the export of certain goods to the country under the Arms Export Control Act ( 22 U.S.C. 2751 et seq. ), the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ), or any other Federal law; and (6) designating the country as a country whose government has repeatedly provided support for acts of international terrorism pursuant to\u2014 (A) section 1754(c)(1)(A)(i) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A)(i) ); (B) section 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 ); (C) section 40(d) of the Arms Export Control Act ( 22 U.S.C. 2780(d) ); or (D) any other provision of law. (f) Rule of Construction Nothing in this section shall be construed to imply that every United States national detained in a country designated as a State Sponsor of Unlawful or Wrongful Detention under subsection (a) should be or is determined to be wrongfully detained under the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act. .",
      "versionDate": "2025-06-26",
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
        "updateDate": "2025-07-24T19:00:52Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4179ih.xml"
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
      "title": "Countering Wrongful Detention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:51Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Countering Wrongful Detention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide the United States Government with additional tools to deter state and non-state actors from wrongfully detaining United States nationals for political leverage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:18:54Z"
    }
  ]
}
```
