# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/818?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/818
- Title: Impeaching Deborah Boardman, Judge of the United States District Court for the District of Maryland, for high crimes and misdemeanors.
- Congress: 119
- Bill type: HRES
- Bill number: 818
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2026-01-28T09:05:43Z
- Update date including text: 2026-01-28T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-10-17 - IntroReferral: Submitted in House
- 2025-10-17 - IntroReferral: Submitted in House
- Latest action: 2025-10-17: Submitted in House

## Actions

- 2025-10-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-10-17 - IntroReferral: Submitted in House
- 2025-10-17 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/818",
    "number": "818",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Impeaching Deborah Boardman, Judge of the United States District Court for the District of Maryland, for high crimes and misdemeanors.",
    "type": "HRES",
    "updateDate": "2026-01-28T09:05:43Z",
    "updateDateIncludingText": "2026-01-28T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
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
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-10-17T18:03:25Z",
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
      "sponsorshipDate": "2025-10-17",
      "state": "OK"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "FL"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "LA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "SC"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "TN"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "CO"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "SC"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "NC"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "PA"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "AZ"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
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
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres818ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 818\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Mr. Roy (for himself, Mr. Brecheen , Mrs. Luna , Mr. Higgins of Louisiana , Mr. Babin , and Mrs. Miller of Illinois ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nImpeaching Deborah Boardman, Judge of the United States District Court for the District of Maryland, for high crimes and misdemeanors.\nThat Deborah Boardman, Judge of the United States District Court for the District of Maryland, is impeached for high crimes and misdemeanors and for violating the constitutional standard for continuance in judicial office of good behavior , and that the following article of removal be exhibited to the United States Senate.\nArticle of impeachment exhibited by the House of Representatives of the United States of America in the name of itself and of the people of the United States of America, against Deborah Boardman, Judge of the United States District Court for the District of Maryland, in maintenance and support of its impeachment against her for high crimes and misdemeanors and for violating the constitutional standard for continuance in judicial office of good behavior .\n#### Article I: Willful and systemic refusal to comply with the law\nJudge Boardman, in violation of her oath of office, did knowingly and willfully use her judicial position to knowingly interfere with the President\u2019s constitutional prerogatives and enforcement of the rule of law.\nThe Constitution grants Congress the authority to create, eliminate, and regulate all Federal courts inferior to the Supreme Court. Section 1 of Article III of the Constitution provides that [t]he Judges, both of the supreme and inferior Courts, shall hold their Offices during good Behavior , thereby granting Congress the authority to remove a judge who fails to remain in good behavior while in office.\nThrough her conduct, in which she violated her oath to the Constitution and duty of impartiality to the people of the United States, Judge Boardman has abused the powers of her judicial authority, having engaged in actions that deviate from the law and toward political ideology as follows:\n**(1)**\nOn October 3, 2025, Judge Boardman sentenced the defendant, Nicholas John Roske, found guilty of attempting to assassinate U.S. Supreme Court Justice Brett Michael Kavanaugh on June 7, 2022, to eight years and a lifetime of supervised release instead of the 30-year sentence recommended by the Department of Justice.\n**(2)**\nRoske traveled by aircraft from his home in Simi Valley, California, to Chevy Chase, Maryland, where Justice Kavanaugh resides with his family, resulting in his arrest outside of Justice Kavanaugh\u2019s home with a firearm with a laser sight attachment, admitting to wanting to inflict harm. Roske was also equipped with zip ties, a tactical knife, pepper spray, a hammer, a screwdriver, a nail punch, a crowbar, duct tape, a pistol light, and was wearing padded boots to minimize noise.\n**(3)**\nRoske spoke to a Montgomery County emergency communication center operator to detail his thoughts while standing outside Justice Kavanaugh\u2019s home. He said that he traveled from California to Maryland to kill a specific United States Supreme Court justice .\n**(4)**\nIn May and June of 2022, before the attempted assassination, Roske\u2019s cell phone history showed repeated internet searches for quietest semi auto rifle, how to quietly knock someone out, most effective place to stab someone, most effective way to silently kill someone, how much force do you need to stab someone\u2019s neck, best way to break into a house, how to make handcuffs with zip ties, and does the secret service protect supreme court justices .\n**(5)**\nThe Department of Justice\u2019s sentencing memorandum of Roske\u2019s detailed how he researched, planned, and attempted to assassinate at least one\u2014but had a stated target of three\u2014sitting judges of the United States Supreme Court .\n**(6)**\nThe Department of Justice also noted Roske intended to \u2026 murder up to three justices in total, and try to evade prosecution by leaving no evidence, claiming an insanity defense, or fleeing to a non-extraditing country .\n**(7)**\nThe Department of Justice outlined Roske\u2019s criminal conduct of attempting to assassination of a Supreme Court Justice required extensive premeditation, as he extensively researched the home addresses of Supreme Court justices and marked their homes on Google Maps, obtained weapons and other tools to eventually use them for killing and traveled across the country with those items, and researched how to infiltrate private residences without detection.\n**(8)**\nRoske attempted to delete any online evidence of motive and intent.\n**(9)**\nJudge Boardman accepted the delusional fiction that Roske\u2014a biological male\u2014has become a woman and then based her sentencing decision on that claim, saying, I take into consideration the conditions of pre-trial confinement and the fact that she is a transgender woman, apparently because the pre-trial detention facility in which Roske was confined does not, of course, indulge this fiction.\n**(10)**\nAttorney General Bondi said of Judge Boardman\u2019s decision, \u2026the judge Boardman also would not refer to the defendant by his biological name .\n**(11)**\nJudge Boardman\u2019s indefensibly light sentence undermines the gravity of the offense committed by Roske and the assault it represented on our Constitution and the rule of law by targeting a Supreme Court Justice.\n**(12)**\nJudge Boardman\u2019s sentencing decision is an egregious instance of a judge allowing her ideology to subvert the TRUTH\u2014which is irreconcilable with the bedrock function of the judicial process and violates the constitutional standard for continuance in judicial office of good behavior.\nThis conduct undermines the orderly functioning of the judiciary by providing an exceptionally low sentence for a defendant who methodically planned to execute multiple assassinations of sitting Supreme Court justices by extensively researching what weapons and tools to procure, researching the home addresses of Supreme Court justices and saving them onto his smart phone, and inquiring how to infiltrate private residences without detection and how to incapacitate and kill individuals.\nAllowing her personal feelings of Roske identifying as a transgender woman to influence her sentencing decision in her high office, Judge Boardman interfered with the will of the people and Congress that have codified statute to impose appropriate sentences for those who intend to kill Federal judges, ignoring the 30-year sentence recommendation by the Department of Justice.\nIn so doing, Judge Boardman used the powers of her position to engage in actions that undermine judicial authority. By making a political decision outside the scope of her legal duties, she compromised the impartiality of our judicial system.\nWherefore, Judge Deborah Boardman is guilty of high crimes and misdemeanors and of conduct that violates the constitute standard of good behavior, and she should be removed from office.",
      "versionDate": "2025-10-17",
      "versionType": "IH"
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
        "name": "Law",
        "updateDate": "2025-12-03T14:00:12Z"
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
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres818ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Impeaching Deborah Boardman, Judge of the United States District Court for the District of Maryland, for high crimes and misdemeanors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T03:48:16Z"
    },
    {
      "title": "Impeaching Deborah Boardman, Judge of the United States District Court for the District of Maryland, for high crimes and misdemeanors.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-18T08:05:58Z"
    }
  ]
}
```
