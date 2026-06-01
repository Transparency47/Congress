# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3900?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3900
- Title: Iran Human Rights, Internet Freedom, and Accountability Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3900
- Origin chamber: Senate
- Introduced date: 2026-02-24
- Update date: 2026-03-13T21:51:39Z
- Update date including text: 2026-03-13T21:51:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in Senate
- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-02-24: Introduced in Senate

## Actions

- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3900",
    "number": "3900",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Iran Human Rights, Internet Freedom, and Accountability Act of 2026",
    "type": "S",
    "updateDate": "2026-03-13T21:51:39Z",
    "updateDateIncludingText": "2026-03-13T21:51:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-24",
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
        "item": {
          "date": "2026-02-24T20:43:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NV"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "UT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "IN"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "MN"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "WV"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NJ"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "AK"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3900is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3900\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2026 Mr. McCormick (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo promote human rights, internet freedom and accountability in Iran, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Iran Human Rights, Internet Freedom, and Accountability Act of 2026 .\n#### 2. Findings; statement of policy\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nFor nearly five decades, the people of Iran have endured brutal repression under the Government of the Islamic Republic of Iran, a regime that denies basic human rights, silences dissidents, and responds to peaceful protest with violence.\n**(2)**\nThe people of Iran have repeatedly and courageously taken to the streets to demand economic opportunity, human rights, dignity, and freedom.\n**(3)**\nDuring the 2026 protests, the Government of the Islamic Republic of Iran responded with brutality by reportedly killing tens of thousands of people and wounding thousands more, arresting tens of thousands, and restricting internet access and telephone lines.\n**(4)**\nThe people of Iran are protesting the Iranian regime\u2019s economic mismanagement, corruption, internal suppression, and unjust executions.\n**(5)**\nAccess to free expression, open information, and uncensored communication are fundamental human rights and critical to the survival of the Iranian protestors.\n**(6)**\nThanks in part to United States-funded efforts to support human rights and open internet access, the Iranian people are consistently found to be one of the most pro-American populations in the Middle East.\n**(7)**\nThe inspiring 2022 Women, Life, Freedom protests demanded an end to the Islamic Republic and its violence, particularly against Iranian women and ethnic minorities.\n**(8)**\nThe barbaric so-called morality police and other arms of state suppression have a lengthy history of repressing the Iranian people\u2019s fundamental freedoms.\n**(9)**\nThe Iranian regime has engaged in systematic efforts to intimidate, harass, detain, and harm political dissidents, activists, and journalists both within Iran and beyond its borders.\n**(10)**\nThe people of Iran deserve the right to dignity, democracy, and self-determination and to be free from the brutality of the Government of the Islamic Republic of Iran.\n##### (b) Statement of policy\nIt shall be the policy of the United States\u2014\n**(1)**\nto recognize the right of the Iranian people to freely determine, through free and fair elections, the future leadership of their country;\n**(2)**\nto facilitate the immediate expansion of unrestricted internet access and civilian lines of communication across Iran;\n**(3)**\nto support the internationally recognized human rights of Iranians and United States programs to assist Iranian civil society, including in their credible documentation, reporting, and accountability efforts of abuses in Iran;\n**(4)**\nto fully enforce sanctions against regime violators of internationally recognized human rights and their family members, including any family members and associates in the United States that continue to directly or indirectly provide support to the regime; and\n**(5)**\nto work in coordination with its allies to consider appropriate measures to deter further lethal violence against protesters.\n#### 3. Improved coordination of efforts to promote internet freedom in Iran\n##### (a) Duties of the Secretary of State\nThe Secretary of State shall be the Federal official with the primary responsibility for\u2014\n**(1)**\npromoting widespread internet freedom in Iran and expanding access to information for Iranian citizens;\n**(2)**\ncoordinating all efforts carried out by Federal departments and agencies that relate to digital freedom initiatives in Iran; and\n**(3)**\nserving as the principal official responsible for updating and carrying out the strategy required under section 414 of the Iran Threat Reduction and Syria Human Rights Act of 2012 ( 22 U.S.C. 8754 ).\n##### (b) Updates to comprehensive strategy To promote internet freedom and access to information in Iran\n**(1) Updates**\nSection 414 of the Iran Threat Reduction and Syria Human Rights Act of 2012 ( 22 U.S.C. 8754 ) is amended\u2014\n**(A)**\nby striking Not later than and inserting (A) Initial strategy .\u2014Not later than ;\n**(B)**\nby redesignating paragraphs (11) and (12) as paragraphs (14) and (15), respectively;\n**(C)**\nby inserting after paragraph (10) the following new paragraphs:\n(11) evaluate the use of virtual private networks and direct-to-cell satellite technologies by civil society and internationally recognized human rights activists in Iran and develop strategies for increasing the accessibility of such networks and technologies; (12) work with the Department of the Treasury and the Department of Commerce to ensure enforcement of sanctions does not impede companies providing to Iranian civilians the technology and other tools necessary to access the open internet; (13) assess the ability of the Iranian regime to cut off all access to the internet and develop a strategy to circumvent internet blackouts for Iranian civil society; ; and\n**(D)**\nby adding at the end of the following new subsection:\n(b) Updates The Secretary of State, in consultation with the Secretary of the Treasury, the Secretary of Commerce, and the heads of other Federal departments and agencies as appropriate, shall review the strategy under subsection (a) on an ongoing basis and update the strategy as appropriate, taking into account the results of such review. .\n**(2) Submission of first updates**\n**(A) Submission**\nNot later than 120 days after the date of the enactment of this Act, the Secretary of State shall\u2014\n**(i)**\nreview and update the strategy pursuant to section 414(b) of the Iran Threat Reduction and Syria Human Rights Act of 2012 ( 22 U.S.C. 8754 ), as added by paragraph (1); and\n**(ii)**\nsubmit such updated strategy to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives.\n**(B) Form**\nThe strategy under subparagraph (A) shall be submitted in an unclassified form, but may include a classified annex.\n#### 4. Internet freedom and censorship circumvention\n##### (a) Internet freedom report\n**(1) In general**\nNot later than 120 days after the date of the enactment of the Act, the Secretary of State, in consultation with the Federal Communications Commission and the Department of the Treasury, shall prepare and submit to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives a report that updates and supplements the report required under section 5124 of the National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ).\n**(2) Additional matters to be included**\nUpdates to the strategy required in section 5124 of the National Defense Authorization Act for Fiscal Year 2025 ( 22 U.S.C. 8754a ) shall also include the following:\n**(A)**\nAn assessment of the feasibility of using direct-to-cell wireless communications technologies to expand internet access for the people of Iran, including technical, regulatory, and security considerations.\n**(B)**\nAn analysis of how drone-based platforms, signal-jamming technologies, and related countermeasures could impact the feasibility, security, economics, and resilience of such direct-to-cell wireless communications.\n**(C)**\nA survey of terrestrial and non-terrestrial telecommunications service providers currently active in Iran, including\u2014\n**(i)**\nwhether such providers are state-owned or state-controlled;\n**(ii)**\nthe extent of foreign participation or investment in such providers;\n**(iii)**\nthe implications of such ownership and control for communications freedom and censorship; and\n**(iv)**\nany other relevant information to assess the opportunities and risks associated with terrestrial and non-terrestrial communications technologies in Iran.\n**(3) Form**\nThe report required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n##### (b) Extension and increase of authorization for Iran Internet Freedom Grant Program\nSection 5124(b)(5)(A) of the National Defense Authorization Act for Fiscal Year 2025 ( 22 U.S.C. 8754a(b)(5)(A) ) is amended by inserting and not less than $20,000,000 for each of fiscal years 2027 through 2030 after $15,000,000 for each of fiscal years 2025 and 2026 .\n##### (c) Development of internet access technologies\n**(1) In general**\nThe Department of State, in coordination with the Department of Defense, the United States Agency for Global Media, and other relevant Federal departments and agencies, shall form a joint working group (referred to as the Working Group ) to support the development of low-cost, easily scalable, and rapidly deployable technologies to counter internet shutdowns or limitations on network access abroad, particularly those imposed by adversary countries, to enable populations to overcome such restrictions.\n**(2) Objectives**\nIn carrying out the responsibilities under subsection (a), the Working Group shall prioritize the following objectives:\n**(A)**\nIdentifying and supporting the development of technologies capable of overcoming internet blackouts and network disruptions imposed by an adversary country and facilitating internet and network access, including\u2014\n**(i)**\nlow-earth orbit satellite internet infrastructure;\n**(ii)**\nmesh networking solutions; and\n**(iii)**\nportable and deployable communication systems.\n**(B)**\nVirtual private networks (commonly known as VPNs ), including\u2014\n**(i)**\ncollaborating with industry, academia, and relevant stakeholders to accelerate the research, development, and deployment of such technologies;\n**(ii)**\nconducting pilot programs and field experiments to test the effectiveness and scalability of developed solutions in real-world settings; and\n**(iii)**\nproviding technical assistance and resources to partner organizations, governments, and nongovernmental entities engaged in efforts to expand internet access.\n**(C)**\nIdentifying and evaluating off-the-shelf technologies that could be rapidly procured and deployed to address internet access challenges in targeted regions.\n**(3) Collaboration with the Federal Acquisition Institute**\nThe Working Group shall collaborate with the Federal Acquisition Institute to leverage expertise in acquisition processes and practices related to carrying out the objectives under paragraph (2) with the aim of\u2014\n**(A)**\nintegrating best practices in defense acquisition into the research, development, and deployment processes of technologies developed by the Working Group to facilitate internet access;\n**(B)**\nensuring that technologies developed by the Working Group align with acquisition priorities and strategies of the Department of State and the Department of Defense;\n**(C)**\nproviding training and educational opportunities for the Working Group on acquisition principles, regulations, and procedures, with a focus on technology development for countering censorship and related restrictions;\n**(D)**\nfostering dialogue and exchange of knowledge between acquisition professionals and innovation specialists to enhance the effectiveness and efficiency of defense technology acquisition related to internet access technologies; and\n**(E)**\ncollaborating on the development of acquisition strategies that prioritize the rapid acquisition and deployment of technologies aimed at countering censorship and restrictions on internet access.\n**(4) Reporting**\nThe Secretary of State, in coordination with the Secretary of Defense and the United States Agency for Global Media, shall submit to the appropriate congressional committees an annual report detailing the progress, challenges, and outcomes of the efforts undertaken pursuant to this section.\n**(5) Authorization of appropriations**\nThere is hereby authorized to be appropriated such sums as may be necessary for each fiscal year 2027 through 2030 to carry out the activities described in this subsection.\n**(6) Appropriate congressional committees defined**\nIn this subsection, the term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services, the Committee on Foreign Relations, and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Armed Services, the Committee on Foreign Affairs, and the Committee on Appropriations of the House of Representatives.\n#### 5. Identification of individuals supporting human rights violations\n##### (a) In general\nNot later than 120 days after receiving a written request from the chairman or ranking member of any of the appropriate congressional committees regarding whether a foreign person has engaged in the conduct described in subsection (b), the President shall\u2014\n**(1)**\ndetermine whether the foreign person has engaged in such conduct; and\n**(2)**\nsubmit to such chairman or ranking minority member a written justification detailing whether the President imposed the sanctions described in subsection (c) with respect to such person.\n##### (b) Conduct described\nThe conduct described in this subsection is knowingly providing material support for the Iranian regime\u2019s abuses of internationally recognized human rights, censorship, or repression of the Iranian people, including\u2014\n**(1)**\nselling, supplying, or transferring censorship technology, surveillance tools, or internet shutdown capabilities;\n**(2)**\nany conduct sanctionable under part 562 of title 31, Code of Federal Regulations (Iranian Human Rights Abuses Sanctions Regulations); or\n**(3)**\nany conduct sanctionable under the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 10101 et seq. ).\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations, the Committee on Armed Services, and the Select Committee on Intelligence of the Senate; and\n**(2)**\nthe Committee on Foreign Affairs, the Committee on Armed Services, and the Permanent Select Committee on Intelligence of the House of Representatives.\n#### 6. Strategy on Iran broadcasting and human rights assistance\n##### (a) Strategy required\n**(1) In general**\nNot later than 120 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Chief Executive Officer of the United States Agency for Global Media, shall submit to the appropriate congressional committees a strategy to expand and enhance United States and international broadcasting efforts and United States programs to support the protection and promotion of internationally recognized human rights in Iran.\n**(2) Elements of the strategy**\nThe strategy required under subsection (a) shall include\u2014\n**(A)**\na comprehensive review and assessment of current United States Government and international broadcasting efforts targeted at Iran, including Voice of America Persian Service, Radio Farda, and other relevant programs, including their reach, effectiveness, and vulnerabilities to Iranian regime censorship, as well as United States Government efforts to support internationally recognized human rights and democratic civil society, including efforts to assist in the credible documentation of abuses of internationally recognized human rights;\n**(B)**\nspecific plans and initiatives to ensure the Iranian people have reliable access to accurate, uncensored, and unbiased news coverage, including through satellite broadcasting, digital circumvention tools, shortwave radio, and emerging technologies;\n**(C)**\nprograms to support independent Iranian journalists, media outlets, and citizen journalists, including grants for equipment, training, secure communication platforms, and capacity-building for Persian and other local language media;\n**(D)**\nprograms to support and train Iranian civil society;\n**(E)**\ncoordination mechanisms with international partners, the private sector, and diaspora communities to amplify credible independent media;\n**(F)**\nannual performance metrics and benchmarks for audience reach, content impact, and program outcomes; and\n**(G)**\na multi-year budget and resource requirements plan to implement the strategy.\n**(3) Form**\nThe strategy required in subsection (a) shall be transmitted in an unclassified form and may contain a classified annex.\n##### (b) GAO report on Near East Regional Democracy (NERD) expenditures\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the appropriate congressional committees a report examining Federal expenditures under the Near East Regional Democracy (NERD) account over fiscal years 2024 and 2025.\n**(2) Matters included**\nThe report shall include\u2014\n**(A)**\na detailed accounting of all NERD funds obligated and expended for Iran-related programs, including broadcasting, media support, civil society assistance, and human rights initiatives;\n**(B)**\nan assessment of the processes used for grant allocation, contractor oversight, vetting of recipients, and measuring program outcomes;\n**(C)**\nan evaluation of the effectiveness of such programs in advancing United States policy objectives, including expanding information access and supporting independent media within Iran; and\n**(D)**\nrecommendations for improving transparency, accountability, and impact measurement.\n##### (c) Form\nThe strategy and the GAO report required under this section shall each be submitted in unclassified form, but may include a classified annex.\n##### (d) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations, the Committee on Armed Services, the Select Committee on Intelligence, and the Committee on Appropriations of the Senate; and\n**(2)**\nthe Committee on Foreign Affairs, the Committee on Armed Services, the Permanent Select Committee on Intelligence, and the Committee on Appropriations of the House of Representatives.\n#### 7. Cybersecurity capacity for civil society in Iran\n##### (a) Training and tools\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall establish programs\u2014\n**(1)**\nto deliver remote or in-person cybersecurity training to journalists, defenders of internationally recognized human rights, and civil-society actors in Iran;\n**(2)**\nto furnish vetted open-source or commercially available digital-safety tools, including VPN services and end-to-end encrypted messaging applications; and\n**(3)**\nto provide multilingual educational materials that warn Iranian users about regime-controlled applications and phishing campaigns.\n##### (b) Reporting and evaluation\n**(1) Quarterly metrics**\nThe Secretary of State shall track and, on a quarterly basis, make available to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives aggregate metrics on the number of trainees, incident-response cases, and unique users of supported digital safety tools.\n**(2) Independent evaluation**\nNot later than 3 years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the appropriate congressional committees an evaluation of the effectiveness of the program carried out under this section.\n##### (c) Savings clause\nNothing in this section may be construed to supersede or limit existing authority under section 404 of the Iran Threat Reduction and Syria Human Rights Act of 2012 ( 22 U.S.C. 8754 ) or any other provision of law related to internet freedom programming in Iran.\n##### (d) Authorization of appropriations\nThere is hereby authorized to be appropriated such sums as may be necessary for each of fiscal years 2027 through 2030 to carry out the activities described in this section.\n#### 8. Rule of construction\nNothing in this Act may be construed as authorizing the use of military force.",
      "versionDate": "2026-02-24",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-03-13T21:51:39Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3900is.xml"
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
      "title": "Iran Human Rights, Internet Freedom, and Accountability Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T10:58:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Iran Human Rights, Internet Freedom, and Accountability Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote human rights, internet freedom and accountability in Iran, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:30Z"
    }
  ]
}
```
