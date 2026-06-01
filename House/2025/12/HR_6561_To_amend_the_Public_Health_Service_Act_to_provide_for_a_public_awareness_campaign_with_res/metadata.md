# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6561?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6561
- Title: PREVENT HPV Cancers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6561
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-21T08:07:59Z
- Update date including text: 2026-05-21T08:07:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6561",
    "number": "6561",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "PREVENT HPV Cancers Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:59Z",
    "updateDateIncludingText": "2026-05-21T08:07:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:01:05Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "NE"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "WA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6561ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6561\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Ms. Castor of Florida (for herself, Mr. Bacon , and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to provide for a public awareness campaign with respect to human papillomavirus, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Resources to Expand Vaccination, Education and New Treatments for HPV Cancers Act of 2025 or the PREVENT HPV Cancers Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe human papillomavirus (referred to in this Act as HPV ) causes six different types of cancer (anal, cervical, oropharynx, penile, vaginal, and vulvar).\n**(2)**\nApproximately 39,300 cases of cancer are caused by HPV each year impacting both women and men.\n**(3)**\nAbout 91 percent of cervical and anal cancers are thought to be caused by HPV.\n**(4)**\nBlack and Hispanic women are more likely to get HPV-associated cervical cancer than women of other races and ethnicities due to disparities in access to cancer screening and early detection.\n**(5)**\nNew cases of cervical cancer decreased among women in young age groups, likely due to HPV vaccination, but in recent years, new cases of cervical cancer rates among women in older age groups have plateaued or, in the case of women ages 30\u201334, increased.\n**(6)**\nCervical cancer screening has declined and there has been an increase in cervical cancer diagnosed at distant stages, which are more difficult to treat and more likely to recur, leading to greater morbidity and mortality.\n**(7)**\nApproximately 70 percent of oropharyngeal cancer is tied to HPV, and such cancers are more than twice as common in men as in women.\n**(8)**\nMost HPV infections that can lead to cancer can be prevented by vaccines.\n**(9)**\nHPV vaccines can also help prevent recurrent respiratory papillomatosis, anal and genital warts.\n**(10)**\nVaccination for HPV is approved for men and women.\n**(11)**\nThe vaccines are most effective if administered when an individual is between the ages of 9 and 12, but the vaccines are licensed for men and women through age 45.\n**(12)**\nApproximately 63 percent of adolescents have completed the HPV vaccine series, a lower rate than other routine recommended vaccinations.\n**(13)**\nAdolescents living in rural areas continue to be less likely to have initiated and completed the HPV vaccine series than those living in urban areas.\n**(14)**\nHealth providers\u2019 recommendation of the vaccine is critical to getting adolescents vaccinated.\n#### 3. HPV cancer prevention public awareness campaign\n##### (a) In general\nSection 317 of the Public Health Service Act ( 42 U.S.C. 247b ) is amended by adding at the end the following new subsection:\n(o) HPV cancer prevention public awareness campaign (1) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall carry out a national campaign to\u2014 (A) increase awareness of the importance of HPV vaccination for preventing HPV-associated cancers; (B) combat misinformation about HPV vaccination; and (C) increase HPV vaccination rates and completion of the vaccine series. (2) Consultation In carrying out the national campaign required by paragraph (1), the Secretary shall consult with the National Academy of Medicine, including health care providers and public health associations, nonprofit organizations (including those that represent communities most impacted by HPV-associated cancers and communities with low vaccination rates), State and local public health departments, elementary and secondary education organizations (including student and parent organizations), and institutions of higher education, to solicit advice on evidence-based information for policy development and program development, implementation, and evaluation. (3) Requirements The national campaign required by paragraph (1) shall\u2014 (A) include the use of evidence-based media and public engagement; (B) be carried out through competitive grants or cooperative agreements awarded to 1 or more nonprofit entities with a history developing and implementing similar campaigns; (C) include the development of culturally and linguistically competent resources that shall be tailored for\u2014 (i) communities with high rates of\u2014 (I) unvaccinated individuals, including males; (II) individuals with high rates of cervical cancer and other HPV-associated cancers (such as Black and Hispanic women); and (III) populations impacted by the increase in oropharynx cancers, including active-duty service members and veterans; (ii) rural communities; and (iii) such other communities as the Secretary determines appropriate; (D) include the dissemination of HPV vaccination information and communication resources to health care providers and health care facilities (including primary care providers, community health centers, dentists, obstetricians, and gynecologists), and such providers and such facilities for pediatric care, State and local public health departments, elementary and secondary schools, and colleges and universities; (E) be complementary to, and coordinated with, any other Federal efforts with respect to\u2014 (i) HPV vaccination; and (ii) screening for HPV-associated cancers, including self-collection methods; (F) include message testing to identify culturally competent and effective messages for behavioral change; and (G) include the award of grants or cooperative agreements to State, local, and Tribal public health departments\u2014 (i) to engage with communities specified in subparagraph (C), local education agencies, health care providers, community organizations, or other groups the Secretary determines are appropriate to develop and deliver effective strategies to increase HPV vaccination rates; and (ii) to disseminate culturally and linguistically competent resources on the National Breast and Cervical Cancer Early Detection Program and where an individual can access the screenings locally. (4) Options for dissemination of information The national campaign required by paragraph (1) may\u2014 (A) include the use of\u2014 (i) social media, television, radio, print, the internet, and other media; (ii) in person or virtual public communications; and (iii) recognized, trusted figures; (B) be targeted to specific groups and communities specified in paragraph (3)(C); and (C) include the dissemination of information highlighting each of the following: (i) Recommended age range to get the HPV vaccine. (ii) The benefits of getting vaccinated against HPV, including the potential to not acquire HPV-associated cancers. (iii) HPV vaccine safety and the systems in place to monitor such safety. (5) Authorization of appropriations There is authorized to be appropriated to carry out this subsection $5,000,000 for each of fiscal years 2026 through 2030. .\n##### (b) Report to Congress\nNot later than September 30, 2027, the Secretary of Health and Human Services shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor and Pensions of the Senate a report\u2014\n**(1)**\nthat contains a qualitative assessment of the campaign under subsection (o) of section 317 of the Public Health Service Act ( 42 U.S.C. 247b ), as added by subsection (a), and the activities conducted under such campaign; and\n**(2)**\non, with respect to the impact on cancer associated with human papillomavirus, the activities conducted under such subsection (o).\n#### 4. Breast and Cervical Cancer Early Detection Program\n##### (a) In general\nSection 1510(a) of the Public Health Service Act ( 42 U.S.C. 300n\u20135(a) ) is amended by striking and $275,000,000 for fiscal year 2012 and inserting $275,000,000 for fiscal year 2012, and $300,000,000 for each fiscal years 2026 through 2030 .\n##### (b) Coordinating committee\nSection 1501(d) of the Public Health Service Act ( 42 U.S.C. 300k(d) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking 2020 and inserting 2030 ; and\n**(2)**\nby striking 2020 and inserting 2030 .",
      "versionDate": "2025-12-10",
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
        "updateDate": "2025-12-12T16:41:30Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6561ih.xml"
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
      "title": "PREVENT HPV Cancers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T14:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PREVENT HPV Cancers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T14:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Resources to Expand Vaccination, Education and New Treatments for HPV Cancers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T14:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to provide for a public awareness campaign with respect to human papillomavirus, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T14:05:38Z"
    }
  ]
}
```
