# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3122?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3122
- Title: Vietnam Human Rights Act
- Congress: 119
- Bill type: HR
- Bill number: 3122
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2025-12-19T09:08:01Z
- Update date including text: 2025-12-19T09:08:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-30 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-30 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3122",
    "number": "3122",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "Vietnam Human Rights Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:08:01Z",
    "updateDateIncludingText": "2025-12-19T09:08:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:05:45Z",
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
          "date": "2025-04-30T14:05:40Z",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
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
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3122ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3122\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Smith of New Jersey (for himself, Mr. Correa , Mr. Tran , and Ms. Lofgren ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo advance United States national interests by prioritizing the protection of internationally recognized human rights and development of the rule of law in relations between the United States and Vietnam, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Vietnam Human Rights Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Findings.\nSec.\u20023.\u2002Statement of policy.\nSec.\u20024.\u2002Sanctions for human rights violations in Vietnam.\nSec.\u20025.\u2002Actions to combat online censorship and surveillance in Vietnam.\nSec.\u20026.\u2002International religious freedom.\nSec.\u20027.\u2002Annual reports on United States-Vietnam human rights dialogue meetings.\nSec.\u20028.\u2002Definitions.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe relationship between the United States and the Socialist Republic of Vietnam has grown substantially since the end of the trade embargo in 1994, with annual trade between the countries reaching $124,000,000,000 in 2023.\n**(2)**\nExpanded economic activity and trade between the United States and Vietnam, has not been matched by greater political freedom or substantial improvements in basic human rights for the people of Vietnam.\n**(3)**\nVietnam remains an authoritarian state ruled by the Communist Party of Vietnam (CPV) which continues to expand cooperation with the Communist Party of China (CCP) for example recently joining General Secretary Xi Jinping\u2019s anti-United States Community of Common Destiny .\n**(4)**\nAccording to the Department of State, the Government of Vietnam engaged the arbitrary arrest of political activists and individuals who protested land seizures or other matters deemed politically sensitive and detained at least 187 persons for political or human rights activism.\n#### 3. Statement of policy\nIt is the policy of the United States to\u2014\n**(1)**\nembed human rights concerns across the full spectrum of official interactions between the Government of the United States and the Government of Vietnam to convey the entire spectrum of United States interests in diplomatic engagement, including that concrete human rights improvements are key parts of trade, security, humanitarian cooperation, and economic development;\n**(2)**\nassess Vietnam\u2019s progress toward respecting the basic rights of workers, as described the report required by section 702 of the Foreign Relations Authorization Act, Fiscal Year 2003 ( Public Law 107\u2013228 ; 22 U.S.C. 2151n note), to ensure that American workers are not disadvantaged by unfair labor practices in Vietnam, and press for Vietnam\u2019s ratification of ILO Conventions No. 87 (Freedom of Association and Protection of the Right to Organize) and No. 98 (Right to Organize and Collective Bargaining) and the recognition of independent labor unions;\n**(3)**\nbar from entry into the United States imports from Vietnam that include inputs made with forced labor from the Xinjiang Uyghur Autonomous Region, such as cotton, aluminum, polysilicon, rayon or other raw or finished materials identified by the Department of Homeland Security, per the Uyghur Forced Labor Prevention Act; and\n**(4)**\nto protect United States nationals and United States businesses by taking steps to address cyber-espionage and transnational repression efforts conducted by Vietnam\u2019s Ministry of Public Security.\n#### 4. Sanctions for human rights violations in Vietnam\n##### (a) Statement of policy\nIt is the policy of the United States to regularly assess reporting from intelligence, diplomatic, open source, congressional, and nongovernmental organization sources to identify and impose travel and financial restrictions on officials of the Government of Vietnam and other foreign persons working directly or indirectly for the Government of Vietnam who, based on credible evidence\u2014\n**(1)**\nare\u2014\n**(A)**\nresponsible for, ordered, or are complicit in the arbitrary detention, torture, enforced disappearances of individuals in Vietnam seeking to obtain, exercise, defend, or promote internationally recognized human rights; or\n**(B)**\nresponsible for, ordered, or are complicit in acts of significant corruption, including the expropriation of private or public assets for personal gain, corruption related to government contracts or the extraction of natural resources, bribery, or the facilitation or transfer of the proceeds of corruption to foreign jurisdictions;\n**(2)**\nare responsible for surveillance, censorship, or detention of individuals in Vietnam for exercising the right to the freedom of expression online or those responsible for forcing United States companies to censor or reveal personally identifiable information of any individual exercising this right; or\n**(3)**\nare responsible for particularly severe violations of religious freedom (as such term is defined in section 3 of the International Religious Freedom Act of 1998 ( 22 U.S.C. 6402 )).\n##### (b) Sanctions\n**(1) Global magnitsky human rights accountability act**\nThe President should impose sanctions under the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 2656 note) with respect to any person described in subsection (a)(1).\n**(2) Department of state, foreign operations, and related programs appropriations act, 2019**\nThe Secretary of State should impose sanctions described in section 7031(c)(1)(A) of the Department of State, Foreign Operations, and Related Programs Appropriations Act, 2019 (division F of the Consolidated Appropriations Act, 2019; Public Law 116\u20136 ) with respect to any person described in subsection (a)(2).\n**(3) Immigration and nationality act**\nThe Secretary of State should impose the sanctions described in section 212(a)(2)(G) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2)(G) ) to any foreign person described in subsection (a)(3).\n##### (c) Report\n**(1) In general**\nThe Secretary of State shall submit to the appropriate congressional committees a report on sanctions imposed on persons described in subsection (a) under the provisions of law described in subsection (b), including information on\u2014\n**(A)**\nthe number of times sanctions were imposed on such persons under such provisions of law;\n**(B)**\nthe reasons for imposing such sanctions; and\n**(C)**\nwhere appropriate, an identification of the sanctioned persons.\n**(2) Inclusion**\nThe report required by this subsection shall be submitted as part of the report required by section of the Foreign Relations Authorization Act, Fiscal Year 2003 ( Public Law 107\u2013228 ; 22 U.S.C. 2151n note).\n#### 5. Actions to combat online censorship and surveillance in Vietnam\n##### (a) Findings\nCongress finds the following:\n**(1)**\nVietnam continues to have one of the world\u2019s most restrictive internet environments, with pervasive filtering of content and the frequent arrests of bloggers and others whose only offense is to advocate online for positions different than those held by the government.\n**(2)**\nSince 2013, the Government of Vietnam has issued laws and decrees, including a cybersecurity law, that increased its ability to surveil its citizens without judicial oversight or recourse. The cybersecurity law has been used to charge Vietnamese citizens with vague crimes of negating revolutionary achievements and distributing misleading information among the people . Vietnam\u2019s Penal Code and Decree 15 have also been used to render many legitimate online activities illegal, leading to the arrest and detentions of political prisoners.\n**(3)**\nVietnam has recently enacted Decree 147, a stringent internet regulation that took effect on December 25, 2024. Decree 147 significantly tightens governmental control over the internet in Vietnam, posing substantial threats to human rights and freedom of speech by enforcing user identification, facilitating state surveillance, and enabling rapid censorship of online content.\n**(4)**\nThe Government of Vietnam uses the cybersecurity law to require United States companies to store information in Vietnam, censor social media posts on demand, and to turn over sensitive personal information about users. Companies such as Facebook and Google comply with these requests, including through the censorship of social media content of United States citizens and permanent resident aliens.\n**(5)**\nUnited States companies Facebook and YouTube have been instrumental in this crackdown, complying with Vietnam\u2019s request to censor and geoblock content determined to violate local Vietnamese law, which often contradicts international law and Vietnam\u2019s treaty obligations.\n**(6)**\nIn the first half of 2020, Facebook increased its content restrictions in Vietnam by 983 percent, a dramatic increase from the second half of 2019.\n**(7)**\nFacebook complied with 90 percent of Vietnam\u2019s censorship requests and YouTube with 95 percent of such requests, a fact the Government of Vietnam noted with satisfaction.\n**(8)**\nAs of December 31, 2023, the local legal provisions that directly enabled Facebook and YouTube\u2019s censorship, Articles 117 and 331 of Vietnam\u2019s Penal Code, were used to imprison most of the 258 prisoners of conscience.\n**(9)**\nA free and open internet and the free flow of news and information\u2014\n**(A)**\nare fundamental components of United States foreign policy because they foster economic growth, protect individual liberties, and advance national security;\n**(B)**\nare critical to the advancement of both United States economic interests and internationally recognized human rights globally; and\n**(C)**\nare severely hindered by Vietnam\u2019s cybersecurity law which would allow the Government of Vietnam to access private data, spy on users, require United States businesses to turn over personally identifiable information or block content of users, including outside of Vietnam, and further restrict already limited online speech.\n##### (b) Statement of policy\nIt is the policy of the United States to\u2014\n**(1)**\npursue an open and free internet in Vietnam as an issue promoting United States economic interests and advancing internationally-recognized human rights;\n**(2)**\nengage all appropriate United States Government agencies to promote the free flow of news and information in Vietnam;\n**(3)**\nuse all appropriate United States diplomatic instruments to pressure the Government of Vietnam to halt requests to force social media companies to disclose identity, or block accounts and content of individuals whose content the Government disapproves;\n**(4)**\nuse all available diplomatic instruments available to pursue trade policies with Vietnam that expand internet freedom and the information economy in Vietnam by\u2014\n**(A)**\nensuring the free flow of information across the global network;\n**(B)**\npromoting stronger international transparency rules; and\n**(C)**\nensuring fair and equal treatment of online services regardless of country of origin; and\n**(5)**\nrequire companies with contracts with the United States Government that accede to requests of the Government of Vietnam to engage in censorship or to reveal sensitive personal information to report such requests to the Department of State at the time such requests occur and to report the nature of such requests and the companies\u2019 responses publicly.\n##### (c) Actions\nThe Secretary of State is authorized to take such actions as may be necessary to\u2014\n**(1)**\nprioritize the immediate distribution of censorship circumvention tools for computers and smartphones in Vietnam; and\n**(2)**\nprioritize projects to ensure the safety and privacy of bloggers and journalists and human rights defenders in Vietnam.\n##### (d) Briefing\nThe Secretary of State, in consultation with the Secretary of Commerce and the United States Trade Representative, should brief the appropriate congressional committees on an action plan outlining efforts to\u2014\n**(1)**\npromote internet freedom and the free flow of news and information in Vietnam; and\n**(2)**\npromote efforts to assist United States internet companies to fulfill their stated missions to promote openness, transparency, and connectivity by opposing requests by the Government of Vietnam to remove political speech or content of journalists, especially when content is removed from the accounts of users in the United States.\n#### 6. International religious freedom\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe promotion and protection of the universally recognized right to the freedom of religion is a priority of United States foreign policy as stated in section 402 of the International Religious Freedom Act of 1998 ( 22 U.S.C. 6442 ) and the Bipartisan Congressional Trade Priorities and Accountability Act of 2015 (title I of Public Law 114\u201326 ; 19 U.S.C. 4201 et seq. ) which requires the Administration to take religious freedom into account when negotiating trade agreements.\n**(2)**\nIn 2024, the United States Commission on International Religious Freedom recommended to the United States Government to designate Vietnam as a country of particular concern , or CPC, for engaging in systematic, ongoing, and egregious violations of religious freedom, as defined by the International Religious Freedom Act (IRFA), and to support legislative efforts to improve religious freedom in Vietnam, including the Vietnam Human Rights Act.\n**(3)**\nOn December 29, 2023, in accordance with the International Religious Freedom Act of 1998, the Secretary of State, for the second consecutive year, placed Vietnam on the Special Watch List for having engaged in or tolerated severe violations of religious freedom.\n##### (b) Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe designation of Vietnam as a country of particular concern for religious freedom pursuant to section 402(b)(1) of the International Religious Freedom Act of 1998 ( 22 U.S.C. 6442(b)(1) ) would be a powerful and effective tool in highlighting abuses of religious freedom in Vietnam and in encouraging improvement in the respect for human rights in Vietnam; and\n**(2)**\nthe Secretary of State should, in accordance with the recommendation of the United States Commission on International Religious Freedom, designate Vietnam as a country of particular concern for religious freedom.\n#### 7. Annual reports on United States-Vietnam human rights dialogue meetings\nSection 702 of the Foreign Relations Authorization Act, Fiscal Year 2003 ( Public Law 107\u2013228 ; 22 U.S.C. 2151n note) is amended by adding at the end the following:\n(9) Ending incidents of torture, police beatings, deaths in police custody, and mob or societal violence targeting religious groups or dissidents. (10) Returning properties of independent religious communities or organizations that have been reportedly expropriated by the Government of Vietnam or by government-sanctioned religious organizations. (11) Addressing individual claims by United States citizens whose properties have been expropriated by the Government of Vietnam without effective, prompt, and fair compensation. (12) Implementing section 4 of the Girls Count Act of ( Public Law 114\u201324 ; 22 U.S.C. 2151 note) and how such section has been applied in Vietnam. (13) Ensuring internet freedom and specific efforts to ensure the safety and privacy of Vietnamese bloggers and journalists on the internet or other forms of electronic communication. .\n#### 8. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nExcept as otherwise provided, the term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate.\n**(2) Internet**\nThe term internet has the meaning given such term in section 231(e)(3) of the Communications Act of ( 47 U.S.C. 231(e)(3) ).\n**(3) Personally identifiable information**\nThe term personally identifiable information means data in a form that identifies a particular person.",
      "versionDate": "2025-04-30",
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
        "updateDate": "2025-05-29T12:05:33Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3122ih.xml"
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
      "title": "Vietnam Human Rights Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T04:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Vietnam Human Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To advance United States national interests by prioritizing the protection of internationally recognized human rights and development of the rule of law in relations between the United States and Vietnam, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:48:20Z"
    }
  ]
}
```
