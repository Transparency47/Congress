# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6262?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6262
- Title: Taiwan Interpol Endorsement and Inclusion Act
- Congress: 119
- Bill type: HR
- Bill number: 6262
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2025-12-18T15:52:37Z
- Update date including text: 2025-12-18T15:52:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6262",
    "number": "6262",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000589",
        "district": "5",
        "firstName": "Lance",
        "fullName": "Rep. Gooden, Lance [R-TX-5]",
        "lastName": "Gooden",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Taiwan Interpol Endorsement and Inclusion Act",
    "type": "HR",
    "updateDate": "2025-12-18T15:52:37Z",
    "updateDateIncludingText": "2025-12-18T15:52:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:05:25Z",
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
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "WI"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "TX"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "NC"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6262ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6262\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Gooden (for himself, Mr. Sherman , Mr. Tiffany , Mr. Lieu , and Mr. Sessions ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo direct the Secretary of State to develop a strategy to obtain membership status for Taiwan in the International Criminal Police Organization, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taiwan Interpol Endorsement and Inclusion Act .\n#### 2. Participation of Taiwan in the International Criminal Police Organization\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nTaiwan is an important contributor to peace and stability around the world.\n**(2)**\nThe Taiwan Relations Act of 1979 ( Public Law 96\u20138 ) states that it is the policy of the United States to preserve and promote extensive, close, and friendly commercial, cultural, and other relations between the people of the United States and the people of Taiwan .\n**(3)**\nThe United States, in the 1994 Taiwan Policy Review, declared its intention to support Taiwan's participation in appropriate international organizations and has consistently reiterated that support.\n**(4)**\nFollowing the enactment of Public Law 108\u2013235 , a law authorizing the Secretary of State to initiate and implement a plan to endorse and obtain observer status for Taiwan at the annual summit of the World Health Assembly and subsequent advocacy by the United States, Taiwan was granted observer status to the World Health Assembly between 2009 and 2016 under the name Chinese Taipei . Both prior to and in its capacity as an observer, Taiwan contributed significantly to the international community's collective efforts in pandemic control, monitoring, early warning, and other related matters. Since 2016, the World Health Assembly has rejected any bids for Taiwan\u2019s inclusion as an observer.\n**(5)**\nSafety, security, and peace is important to every citizen of the world, and shared information ensuring wide assistance among police authorities of nations for expeditious dissemination of information regarding criminal activities greatly assists in these efforts.\n**(6)**\nDirect and unobstructed participation in the International Criminal Police Organization (Interpol) is beneficial for all nations and their police authorities. Internationally shared information with authorized police authorities are vital to peacekeeping efforts.\n**(7)**\nWith a history dating back to 1914, the role of Interpol is defined in its constitution: To ensure and promote the widest possible mutual assistance between all criminal police authorities within the limits of the laws existing in the different countries and in the spirit of the Universal Declaration of Human Rights. .\n**(8)**\nOngoing international threats, including international networks of terrorism, show the ongoing necessity to be ever inclusive of nations willing to work together to combat criminal activity. The ability of police authorities to coordinate, preempt, and act swiftly and in unison is an essential element of crisis prevention and response.\n**(9)**\nTaiwan maintained full membership in Interpol starting in 1964 through its National Police Administration but was ejected in 1984 when the People's Republic of China (PRC) applied for membership.\n**(10)**\nNonmembership in Interpol prevents Taiwan from gaining access to Interpol\u2019s I\u201324/7 global police communications system, which provides real-time information on criminals and global criminal activities. Taiwan is relegated to second-hand information from friendly nations, including the United States.\n**(11)**\nTaiwan is unable to swiftly share information on criminals and suspicious activity with the international community, leaving a huge void in the global crime-fighting efforts and leaving the entire world at risk.\n**(12)**\nInterpol\u2019s constitution allows for observers at its meetings by police bodies which are not members of the Organization .\n##### (b) Statement of policy\nIt should be the policy of the United States\u2014\n**(1)**\nto advocate, as appropriate\u2014\n**(A)**\nfor Taiwan\u2019s membership in all international organizations, including Interpol, and in which the United States is also a participant; and\n**(B)**\nfor Taiwan to be granted full membership status in other appropriate international organizations;\n**(2)**\nto instruct, as appropriate, representatives of the United States Government in all organizations described in paragraph (1) to use the voice, vote, and influence of the United States to advocate for Taiwan's membership or observer status in such organizations; and\n**(3)**\nfor the President or the President's designees to advocate, as appropriate, for Taiwan's membership or observer status in all organizations described in paragraph (1) as part of any relevant bilateral engagements between the United States and the People's Republic of China, including leader summits and the U.S.-China Comprehensive Economic Dialogue.\n##### (c) Taiwan\u2019s participation in Interpol\nThe Secretary of State shall\u2014\n**(1)**\ndevelop a strategy to\u2014\n**(A)**\nobtain membership status for Taiwan in Interpol and at other related meetings, activities, and mechanisms thereafter;\n**(B)**\nencourage meaningful interaction, including information sharing, with U.S. National Central Bureau (Interpol Washington) and Taiwan on issues related to global crime fighting;\n**(C)**\ninvolve Taiwan in Interpol meetings, events, and related activities; and\n**(D)**\nin certain cases as appropriate and in alignment with United States interests, assist Taiwan in increasing its economic, security, and diplomatic engagement with countries in the Indo-Pacific region and around the world; and\n**(2)**\ninstruct Interpol Washington to officially request membership status for Taiwan in Interpol and to actively urge Interpol member states to support such membership status and participation for Taiwan.\n##### (d) Report\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State, in coordination with Interpol Washington, shall transmit to Congress a report, in unclassified form, describing the United States strategy to endorse and obtain observer status or membership status for Taiwan in appropriate international organizations, including Interpol, and at other related meetings, activities, and mechanisms thereafter. The report shall include the following:\n**(1)**\nA description of the efforts the Secretary has made to encourage member states to promote Taiwan's bids to obtain observer status or membership status in appropriate international organizations, including Interpol.\n**(2)**\nA description of the actions the Secretary will take to endorse and obtain observer status or membership status for Taiwan in appropriate international organizations, including Interpol, and at other related meetings, activities, and mechanisms thereafter.\n#### 3. Report\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the U.S. National Central Bureau (Interpol Washington) shall submit to the Committee on the Judiciary of the House of Representatives and the Committee on the Judiciary of the Senate a report on any and all threats posed to Taiwan\u2019s criminal intelligence as a result of their non-member and non-observer status in the International Criminal Police Organization (Interpol) and, therefore, Taiwan\u2019s lack of access to Interpol communications and data.\n##### (b) Form\nThe report required by subsection (a) shall be submitted in unclassified form, but may contain a classified annex.",
      "versionDate": "2025-11-21",
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
        "updateDate": "2025-12-18T15:52:37Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6262ih.xml"
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
      "title": "Taiwan Interpol Endorsement and Inclusion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Taiwan Interpol Endorsement and Inclusion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of State to develop a strategy to obtain membership status for Taiwan in the International Criminal Police Organization, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:25Z"
    }
  ]
}
```
