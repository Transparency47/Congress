# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2700?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2700
- Title: UNPLUGGED Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2700
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2700",
    "number": "2700",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "UNPLUGGED Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2700ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2700\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Vindman introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require State educational agencies to implement policies prohibiting the use or possession of personal mobile phones by students in public school classrooms during school hours, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Utilize No Phones in Learning to Unleash Growth in Grades and Educate Distraction-free Act of 2025 or the UNPLUGGED Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nPublic education is critical to the economic vitality, national security, and democratic governance of the United States.\n**(2)**\nDisruptions to the educational process directly affect national productivity, civic engagement, and workforce development.\n**(3)**\nThe excessive use of mobile phones during school hours significantly impairs the ability of schools to maintain effective educational environments.\n**(4)**\nA growing body of peer-reviewed literature has documented the detrimental effects of mobile phone usage in classrooms on attention, academic performance, and mental health.\n**(5)**\nStudies published in journals such as Computers in Human Behavior, Educational Psychology, and the Journal of Adolescent Health have shown that the presence of mobile phones in academic settings correlates with reduced focus, lower test scores, increased academic procrastination, and higher levels of anxiety and depression among students.\n**(6)**\nSocial psychologist Jonathan Haidt, in both his academic work and public commentary, has\u2014\n**(A)**\nextensively documented the relationship between the rise of smartphone use among adolescents and the decline in mental health indicators;\n**(B)**\nproduced research pointing to a sharp increase in rates of anxiety, depression, and self-harm beginning around 2012\u20132013, coinciding with widespread smartphone and social media adoption among teenagers; and\n**(C)**\nargued that overexposure to digital devices and online platforms undermines the development of resilience, emotional regulation, and in-person social connection.\n**(7)**\nLimiting in-school phone access is essential to reversing harmful psychological and academic trends in American youth.\n**(8)**\nThe presence of mobile phones in educational settings contributes to increased rates of bullying, cyber harassment, academic dishonesty, and classroom distractions, thereby undermining the core mission of public education.\n**(9)**\nThese issues are not confined to a single state or region and are national in scope, with similar patterns of disruption and diminished student outcomes reported across state lines.\n**(10)**\nThe cumulative effect of diminished educational achievement has a substantial impact on the national economy and workforce preparedness.\n##### (b) Sense of Congress\nIt is the sense of Congress that each State educational agency, in coordination with each local educational agency served by the State educational agency and in consultation with educators, parents, and students, should establish and enforce a policy that\u2014\n**(1)**\nenables parents to notify students through school officials about forgotten items, changes in pick-up times, and other common issues; and\n**(2)**\nenables schools to communicate with parents regarding time-sensitive items.\n#### 3. Prohibition of student phone possession in schools\n##### (a) In general\nNot later than the first school year beginning after the date of enactment of this Act, each State educational agency, in coordination with each local educational agency served by the State educational agency and in consultation with educators, parents, and students, shall establish and enforce a policy that prohibits student possession or use of personal electronic devices, including personal mobile phones, in public schools during school hours.\n##### (b) Secure storage methods\nA personal electronic device policy established pursuant to subsection (a) may include a requirement that public schools use secure storage methods, including\u2014\n**(1)**\nlockable lockers;\n**(2)**\nsecure lock boxes;\n**(3)**\nmagnetic pouches or other signal-blocking storage devices; or\n**(4)**\nother technologies or materials deemed appropriate by the State educational agency.\n##### (c) Exceptions\nA personal electronic device policy established pursuant to subsection (a) may permit exceptions for\u2014\n**(1)**\nstudents with medical or health conditions that require the use of a mobile phone or other personal electronic device as part of a treatment or monitoring plan, as certified by a licensed healthcare provider;\n**(2)**\nstudents with disabilities or special needs for whom access to a personal mobile phone or other personal electronic device is\u2014\n**(A)**\ndocumented as necessary in an individualized education program; or\n**(B)**\nincluded as part of services or accommodations provided to the student pursuant to section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ) (commonly referred to as a Section 504 plan );\n**(3)**\non an individualized basis for students\u2014\n**(A)**\nwho are English learners;\n**(B)**\nwho have a demonstrated need for a personal electronic device to facilitate instruction; and\n**(C)**\nacquire documentation in support of subparagraph (A) and (B) in accordance with procedures established by the State educational agency; and\n**(4)**\nadditional situations as States and local education authorities deem necessary and appropriate.\n##### (d) Minimum requirement\nThe requirements in this Act shall constitute a minimum standard. Nothing in this Act shall be construed to preempt or prevent a State, State educational agency, or local educational agency from enacting more restrictive policies regarding student possession or use of mobile phones or other personal electronic devices during school hours, on school grounds, or during school activities.\n##### (e) Grant program authorized\n**(1) In general**\nThe Secretary of Education shall establish a grant program to provide funding to State educational agencies to purchase, implement, or maintain secure storage methods, and related training or infrastructure, in accordance with a personal electronic device policy established by such State educational agency pursuant to subsection (a).\n**(2) Application**\nTo be eligible to receive a grant under this subsection, a State educational agency shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n#### 4. Definitions\nFor purposes of this Act:\n**(1) ESEA terms**\nThe terms elementary school , English learner , local educational agency , secondary school , State , and State educational agency have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Individualized education program**\nThe term individualized education program has the meaning given such term in section 602 of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 ).\n**(3) Mobile phone**\nThe term mobile phone means any handheld communication device with cellular, Wi-Fi, or Bluetooth capability, including smartphones and similar devices.\n**(4) Personal electronic device**\nThe term personal electronic device \u2014\n**(A)**\nincludes mobile phones, smartwatches, tablets, and other handheld or wearable devices with communication, internet, or multimedia capabilities; and\n**(B)**\ndoes not include laptops or tablets that are authorized by the school and used solely for instructional purposes under teacher supervision so long as such laptops or tablets are restricted from accessing social media platforms, personal email, messaging or texting services, and other non-academic applications during instructional time.\n**(5) Public school**\nThe term public school means\u2014\n**(A)**\na public elementary school; and\n**(B)**\na public secondary school.\n**(6) School hours**\nThe term school hours means the period from the start of the instructional day until the end of the instructional day, as defined by the State educational agency.",
      "versionDate": "2025-04-07",
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
        "name": "Education",
        "updateDate": "2025-05-05T12:17:26Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2700ih.xml"
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
      "title": "UNPLUGGED Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "UNPLUGGED Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Utilize No Phones in Learning to Unleash Growth in Grades and Educate Distraction-free Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require State educational agencies to implement policies prohibiting the use or possession of personal mobile phones by students in public school classrooms during school hours, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:20Z"
    }
  ]
}
```
